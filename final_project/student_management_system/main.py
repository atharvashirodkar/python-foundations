from file_handler import load_students, save_students
from menu import show_menu
from models.student import Student
from utils.display import display_student
from validators import validate_student_id, validate_name, validate_age, validate_course


def add_student():
    students = load_students()

    try:

        student_id = validate_student_id(input("Enter Student ID: "))

        name = validate_name(input("Enter Name: "))

        age = validate_age(int(input("Enter Age: ")))

        course = validate_course(input("Enter Course: "))

    except ValueError as e:

        print(f"Error: {e}")
        return

    # Duplicate ID check
    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists")
            return

    new_student = Student(student_id, name, age, course)

    students.append(new_student.to_dict())

    save_students(students)

    print("Student added successfully")


def view_students():
    students = load_students()

    if not students:
        print("No students found")
        return

    for student in students:
        display_student(student)
        print("-" * 40)


def search_student():
    students = load_students()

    search_id = input("Enter Student ID: ")

    for student in students:
        if student["student_id"] == search_id:
            print("\nStudent Found")
            print("-" * 40)

            print(f"ID     : {student['student_id']}")
            print(f"Name   : {student['name']}")
            print(f"Age    : {student['age']}")
            print(f"Course : {student['course']}")

            print("-" * 40)

            return

    print("Student not found")


def update_student():
    students = load_students()

    update_id = input("Enter Student ID to update: ")

    for student in students:
        print(student["student_id"] == update_id)
        if student["student_id"] == update_id:

            print("Leave blank to keep old value")

            new_name = input(f"Enter New Name ({student['name']}): ")
            new_age = int(input(f"Enter New Age ({student['age']}): "))
            new_course = input(f"Enter New Course ({student['course']}): ")

            if new_name:
                student["name"] = new_name

            if new_age:
                student["age"] = new_age

            if new_course:
                student["course"] = new_course

            save_students(students)

            print("Student updated successfully")

            return

    print("Student not found")


def delete_student():
    students = load_students()

    delete_id = input("Enter Student ID to delete: ")

    updated_students = []

    found = False

    for student in students:

        if student["student_id"] == delete_id:
            found = True
            continue

        updated_students.append(student)

    confirm = input("Are you sure? (y/n): ").lower()

    if confirm != "y":
        return

    if found:
        save_students(updated_students)
        print("Student deleted successfully")
    else:
        print("Student not found")


def main():

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            print("Exiting Program...")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
