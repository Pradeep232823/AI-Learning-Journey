from fastapi import HTTPException, Path, Depends, APIRouter
from database import db_connect
from schemas import StudentCreate, StudentResponse
from services import student_service

router = APIRouter(prefix="/students", tags=["students"])

def get_db():
    db_name = "students.db"
    conn = db_connect(db_name)
    try:
        yield conn
    finally:
        conn.close()

def student_response(student):
    return StudentResponse(
        student_id=student[0],
        name=student[1],
        department=student[2]
    )

@router.post("", response_model=StudentResponse, status_code=201)
def create_student(student : StudentCreate, conn = Depends(get_db)):

    inserted_student, error = student_service.create_student(conn, student.name, student.department)
    
    if error:
        raise HTTPException(
            status_code=400,
            detail=error
        )

    return student_response(inserted_student)

@router.get("", response_model=list[StudentResponse])
def read_students(conn = Depends(get_db)):

    students = student_service.get_students(conn)
    return [
        student_response(student)
        for student in students
    ]

@router.get("/{student_id}", response_model=StudentResponse)
def read_student_by_id(student_id : int = Path(gt=0), conn = Depends(get_db)):

    student_data = student_service.get_student_by_id(conn, student_id)

    if student_data is not None:
        return student_response(student_data)
    else:
        raise HTTPException(
            status_code=404,
            detail="Student data not found"
        )

@router.put("/{student_id}", response_model=StudentResponse)
def update_student(student : StudentCreate, student_id : int = Path(gt=0), conn = Depends(get_db)):

    updated_student = student_service.update_student(conn, student_id, student.name, student.department)

    if updated_student is not None:
        return student_response(updated_student)
    else:
        raise HTTPException(
            status_code=404,
            detail="Student data not found to update"
        )

@router.delete("/{student_id}", response_model=StudentResponse)
def delete_student(student_id : int = Path(gt=0), conn = Depends(get_db)):

    deleted_student = student_service.delete_student(conn, student_id)

    if deleted_student is not None:
        return student_response(deleted_student)
    else:
        raise HTTPException(
            status_code=404,
            detail="Student data not found to delete"
        )