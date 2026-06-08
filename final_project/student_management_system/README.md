# Student Management System

A terminal-based Student Management System built using Python.

This project serves as the capstone project for the Python Programming Foundations curriculum and demonstrates the practical application of core Python concepts including Object-Oriented Programming (OOP), file handling, exception handling, modules, packages, and JSON data persistence.

---

## Features

- Add Student
- View All Students
- Search Student by ID
- Update Student Information
- Delete Student Records
- Data Persistence using JSON
- Input Validation
- Exception Handling
- Modular Project Structure

---

## Why This Project Is Useful

This project combines multiple Python concepts into a single real-world application.

### Concepts Demonstrated

- Variables and Data Types
- Functions
- Conditional Statements
- Loops
- Lists and Dictionaries
- File Handling
- JSON Operations
- Exception Handling
- Object-Oriented Programming
- Modules and Packages

It provides a practical example of organizing Python code across multiple files instead of writing everything in a single script.

---

## Project Structure

```text
student_management_system/
│
├── main.py
├── menu.py
├── file_handler.py
├── validators.py
│
├── models/
│   ├── __init__.py
│   └── student.py
│
├── utils/
│   ├── __init__.py
│   └── display.py
│
├── data/
│   └── students.json
│
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10 or later

Check your Python version:

```bash
python --version
```

### Run the Application

Navigate to the project directory:

```bash
cd student_management_system
```

Run:

```bash
python main.py
```

---

## Example Usage

```text
========= STUDENT MANAGEMENT SYSTEM =========

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

=============================================
```

Example student record:

```json
{
    "student_id": "S101",
    "name": "John Doe",
    "age": 20,
    "course": "Python"
}
```

---

## Data Storage

Student records are stored locally in:

```text
data/students.json
```

The application automatically reads from and writes to this file during CRUD operations.

---

## Learning Outcomes

After building this project, you should understand:

- How to structure a Python project
- How modules interact with each other
- How to persist data using JSON
- How to validate user input
- How to handle runtime errors gracefully
- How to design a simple terminal-based application

---

## Getting Help

If you encounter issues:

1. Verify that Python is installed correctly.
2. Ensure you are running the application from the project root directory.
3. Check terminal error messages for debugging information.
4. Review the corresponding modules in the Python Programming Foundations repository.

---

## Contributing

This project was created as part of a learning curriculum.

Contributions, improvements, and refactoring suggestions are welcome.

### Contribution Guidelines

- Keep the code beginner-friendly.
- Follow the existing project structure.
- Maintain clear and readable code.
- Add comments only when necessary to improve understanding.

---

## Author

Created and maintained by **Atharva Shirodkar**  
GitHub: [@atharvashirodkar](https://github.com/atharvashirodkar)

Maintained as part of the Python Programming Foundations learning repository.