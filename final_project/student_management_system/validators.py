def validate_student_id(student_id):
    if not student_id.strip():
        raise ValueError("Student ID cannot be empty")

    return student_id.strip()

def validate_name(name):
    if not name.strip():
        raise ValueError("Name cannot be empty")

    return name.strip().title()

def validate_age(age):
    age = int(age)

    if age < 1 or age > 120:
        raise ValueError("Age must be between 1 and 120")

    return age

def validate_course(course):
    if not course.strip():
        raise ValueError("Course cannot be empty")

    return course.strip().title()

