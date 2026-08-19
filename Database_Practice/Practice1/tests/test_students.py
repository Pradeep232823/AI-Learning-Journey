import sqlite3
import pytest

from fastapi.testclient import TestClient

from main import app
from routers.students import get_db

def override_get_db():
    conn = sqlite3.connect("test_students.db")
    try:
        yield conn
    finally:
        conn.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app, raise_server_exceptions=False)

def create_test_database():
    conn = sqlite3.connect("test_students.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            department TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

create_test_database()

@pytest.fixture
def test_db():
    conn = sqlite3.connect("test_students.db")

    conn.execute("DELETE FROM students")
    conn.execute("DELETE FROM sqlite_sequence WHERE name = 'students'")

    conn.commit()

    yield conn

    conn.close()

@pytest.fixture
def student(test_db):
    response = client.post(
        "/students",
        json={
            "name": "Test Student",
            "department": "Computer Science"
        }
    )

    assert response.status_code == 201

    return response.json()

def test_create_student(test_db):
    response = client.post(
        "/students",
        json={
            "name": "Test Student",
            "department": "Computer Science"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["name"] == "Test Student"
    assert data["department"] == "Computer Science"
    assert "student_id" in data

def test_create_student_invalid_data(test_db):
    response = client.post(
        "/students",
        json={
            "name": "",
            "department": "Computer Science"
        }
    )

    assert response.status_code == 422

def test_create_student_invalid_name(test_db):
    response = client.post(
        "/students",
        json={
            "name": 12345,
            "department": "Computer Science"
        }
    )

    assert response.status_code == 422

def test_get_students(test_db):
    client.post(
        "/students",
        json={
            "name": "Test Student",
            "department": "Computer Science"
        }
    )

    response = client.get("/students")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["name"] == "Test Student"
    assert data[0]["department"] == "Computer Science"

def test_get_student_by_id(student):
    student_id = student["student_id"]

    response = client.get(f"/students/{student_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["student_id"] == student_id
    assert data["name"] == "Test Student"
    assert data["department"] == "Computer Science"

def test_get_student_by_id_not_found(test_db):
    response = client.get("/students/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student data not found"

def test_update_student(student):
    student_id = student["student_id"]

    response = client.put(
        f"/students/{student_id}",
        json={
            "name": "Updated Name",
            "department": "Information Technology"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["student_id"] == student_id
    assert data["name"] == "Updated Name"
    assert data["department"] == "Information Technology"

def test_update_student_not_found(test_db):
    response = client.put(
        "/students/999",
        json={
            "name": "Updated Name",
            "department": "Information Technology"
        }
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Student data not found to update"

def test_delete_student(student):
    student_id = student["student_id"]

    response = client.delete(f"/students/{student_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["student_id"] == student_id
    assert data["name"] == "Test Student"
    assert data["department"] == "Computer Science"

def test_delete_student_not_found(test_db):
    response = client.delete("/students/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Student data not found to delete"

def override_get_db_error():
    raise Exception("Database connection failed")

def test_internal_server_error():
    app.dependency_overrides[get_db] = override_get_db_error
    try:
        response = client.get("/students")

        assert response.status_code == 500
        assert response.json()["detail"] == "Internal server error"
    finally:
        app.dependency_overrides[get_db] = override_get_db