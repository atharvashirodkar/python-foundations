# Mini Project 05: Library Management System

## Objective

Build a console-based library management system using Object-Oriented Programming.

---

## Features

1. Add Book
2. View Books
3. Search Book
4. Issue Book
5. Return Book
6. Remove Book
7. Exit

---

## Book Information

Store:

- Book ID
- Title
- Author
- Availability Status

---

## Requirements

- Use a Book class.
- Prevent issuing unavailable books.
- Prevent returning books that are already available.
- Validate user input.
- Organize the project into multiple files.

---

## Suggested Structure

```text
library_management_system/
│
├── main.py
├── file_handler.py
├── models/
│   └── book.py
└── data/
    └── books.json
```

---

## Bonus Challenge

Store all data in a JSON file and load it automatically when the program starts.

---

## Concepts Practiced

- OOP
- File Handling
- Modules
- Exception Handling
- JSON
- Project Structure