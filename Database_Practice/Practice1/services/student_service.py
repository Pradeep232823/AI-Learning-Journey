import student_repository


def create_student(conn, name, department):
    return student_repository.insert_student(
        conn,
        name,
        department
    )

def get_students(conn):
    return student_repository.show_students(conn)


def get_student_by_id(conn, student_id):
    return student_repository.get_student_by_id(
        conn,
        student_id
    )

def update_student(conn, student_id, name, department):
    return student_repository.update_student(
        conn,
        student_id,
        name,
        department
    )


def delete_student(conn, student_id):
    return student_repository.delete_student(
        conn,
        student_id
    )