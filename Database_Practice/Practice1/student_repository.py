import validators

def insert_student(conn, name, department):
    cursor = None
    try:
        valid_name = validators.validate_name(name.strip())
        valid_department = validators.validate_department(department.strip())

        if valid_name is None or valid_department is None:
            return None, "Invalid name or department"

        cursor = conn.cursor()

        values = (valid_name, valid_department)

        query = "INSERT INTO students (name, department) values (?, ?)"

        cursor.execute(query, values)

        conn.commit()

        student_id = cursor.lastrowid

        cursor.execute("SELECT * FROM students WHERE student_id = ?",(student_id,))

        student = cursor.fetchone()

        return student, None
        
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
        raise

    finally:
        if cursor:
            cursor.close()


def show_students(conn):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students")

        students = cursor.fetchall()

        return students
        
    except Exception as e:
        print(f"Error occurred: {e}")
        raise

    finally:
        if cursor:
            cursor.close()

def update_student(conn, student_id, name, department):
    cursor = None
    try:

        valid_name = validators.validate_name(name.strip())
        valid_department = validators.validate_department(department.strip())
        if valid_name is None or valid_department is None:
            return None
        valid_student_id = validators.validate_student_id(student_id)
        if valid_student_id is None:
            return None
        
        student = get_student_by_id(conn, valid_student_id)
        if student is None:
            return None
        
        cursor = conn.cursor()

        values = (valid_name, valid_department, valid_student_id)

        query = "UPDATE students SET name = ?, department = ? WHERE student_id = ?"

        cursor.execute(query, values)

        conn.commit()

        student = get_student_by_id(conn, valid_student_id)

        return student
        
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
        raise

    finally:
        if cursor:
            cursor.close()

def delete_student(conn, student_id):
    cursor = None
    try:
        valid_student_id = validators.validate_student_id(student_id)
        if valid_student_id is None:
            return None
        
        student = get_student_by_id(conn, valid_student_id)
        if student is None:
            return None
        
        
        cursor = conn.cursor()

        query = "DELETE FROM students WHERE student_id = ?"
        cursor.execute(query, (valid_student_id,))
        conn.commit()

        return student
        
    except Exception as e:
        conn.rollback()
        print(f"Error occurred: {e}")
        raise

    finally:
        if cursor:
            cursor.close()

def get_student_by_id(conn, student_id):
    cursor = None
    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM students WHERE student_id = ?",(student_id,))

        student = cursor.fetchone()

        return student

    except Exception as e:
        print(f"Error occurred: {e}")
        raise

    finally:
        if cursor:
            cursor.close()