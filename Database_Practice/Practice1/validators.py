def validate_student_id(student_id):
    if isinstance(student_id, int) and student_id > 0:
        return student_id
    else:
        return None


def validate_name(name):
    if isinstance(name, str) and name:
        return name
    else:
        return None

def validate_department(department):
    if isinstance(department, str) and department:
        return department
    else:
        return None