# 📚 Python Programming Foundations

A comprehensive, hands-on learning module designed to build a **solid foundation in Python programming**. From basic syntax to object-oriented design principles, this course covers essential concepts with practical exercises, real-world projects, and interview preparation material.

---

## 💡 Why It Matters

**Python** is one of the most accessible and versatile programming languages today. Whether you're building web applications, analyzing data, or automating tasks, mastering the fundamentals is crucial. This module provides:

- **Structured Learning Path** – Progresses logically from basic concepts to advanced OOP and design patterns
- **Hands-On Practice** – Every concept includes practical exercises and real-world problem-solving scenarios
- **Interview Ready** – Includes interview questions and solutions to prepare for technical assessments
- **Industry Best Practices** – Learn clean code principles, error handling, and professional development workflows
- **Real Projects** – Apply your knowledge through mini-projects and a comprehensive final project

---

## 📖 Course Structure

### **Beginner Level**

| Module | Topics | Files |
|--------|--------|-------|
| **01 – Intro to Python** | Variables, data types, input/output, type casting | `intro.py`, `simple_calculator.py`, `swap_num.py` |
| **02 – Operators & Conditionals** | Arithmetic, comparison, logical operators; if/else; match-case | `01_operators.py`, `02_conditional_statements.py`, `03_match_case.py` |
| **03 – Loops & Iterations** | For loops, while loops, loop control; pattern generation | `loops.py`, practice problems: factorial, fibonacci, password check |

### **Intermediate Level**

| Module | Topics | Files |
|--------|--------|-------|
| **04 – Functions** | Function definition, parameters, return values, lambda, recursion | `01_function_basics.py` through `05_recursion.py` |
| **05 – Strings, Lists & Tuples** | String methods, slicing, formatting; list operations; tuple unpacking | Multiple submodules: `01_string/`, `02_lists/`, `03_tuples/` |
| **06 – Dicts, Sets & Algorithms** | Dictionary operations, set operations, searching and sorting algorithms | `01_dictionaries/`, `02_sets/`, `03_searching/`, `04_sorting/` |

### **Advanced Level**

| Module | Topics | Files |
|--------|--------|-------|
| **07 – Files & Exceptions** | File I/O, error handling, exception management | `01_file_operations/`, `02_exception_handling/` |
| **08 – Object-Oriented Programming** | Classes, objects, constructors, encapsulation | `01_classes_objects.py` through `05_encapsulation.py` |
| **09 – Advanced OOP** | Inheritance, polymorphism, method overriding, abstraction | `01_inheritance.py` through `04_abstraction.py` |
| **10 – Modules & Packages** | Importing modules, creating packages, virtual environments | `01_importing_modules.py` through `05_virtual_environments.md` |

---

## ⚙️ Getting Started

### **Prerequisites**

- **Python 3.8+** installed on your system
- A code editor (VS Code, PyCharm, or similar)
- Basic command-line familiarity
- A curious mind ready to learn!

### **Installation & Setup**

1. **Clone or Download** the repository:
   ```bash
   git clone <repository-url>
   cd module_1_programming_foundations
   ```

2. **Verify Python Installation**:
   ```bash
   python --version
   ```

3. **Run a Simple Script** to test setup:
   ```bash
   python 01_intro_python/intro.py
   ```

4. **(Optional) Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate      # On Windows
   ```

### **Learning Path Recommendation**

Follow modules in numerical order:

1. Start with **Module 01** to get comfortable with basic Python syntax
2. Build logic skills with **Modules 02-03** (operators, conditionals, loops)
3. Master functions and data structures in **Modules 04-06**
4. Progress to **Modules 07-10** for professional-level programming
5. Apply everything in the **Mini Projects** and **Final Project**

### **Example Usage**

**Run a beginner script**:
```bash
python 01_intro_python/simple_calculator.py
```

**Explore functions and recursion**:
```bash
python 04_functions/05_recursion.py
```

**Practice OOP concepts**:
```bash
python 08_oop/01_classes_objects.py
```

**Run the final student management project**:
```bash
python final_project/student_management_system/main.py
```

---

## 🎯 Key Learning Outcomes

By completing this module, you'll be able to:

✅ Write clean, readable Python code following best practices  
✅ Solve problems using loops, conditionals, and functions  
✅ Work with complex data structures (lists, dicts, sets, tuples)  
✅ Design and implement object-oriented solutions  
✅ Handle files and exceptions gracefully  
✅ Create modular, reusable code with packages  
✅ Build complete applications from scratch  
✅ Answer technical interview questions with confidence  

---

## 📁 Project Highlights

### **Mini Projects**
Get practical experience with small, focused projects:
- 💰 **Calculator App** – Build an interactive calculator
- 👨‍🎓 **Student Record System** – Manage student data with CRUD operations
- 📁 **File Manager** – Create, read, and organize files programmatically
- 📦 **Inventory Management System** – Track products and stock levels
- 📚 **Library Management System** – Implement a book lending system

### **Final Project: Student Management System**
A comprehensive CLI (Command Line Interface) application demonstrating:
- Object-oriented design patterns
- File handling and data persistence
- Exception handling and validation
- Modular architecture (`models/`, `utils/`, `data/`)
- Real-world business logic

---

## 📚 Resources & Support

### **Additional Learning Materials**

- **Cheatsheets**: Check module folders for `.md` cheatsheets (e.g., `08_oop/oop_cheatsheet.md`)
- **Interview Questions**: Find preparation materials in `interview_questions.md` files
- **Practice Problems**: Each module includes dedicated `practice/` or `practice_questions/` folders

### **Where to Get Help**

- 📖 **Python Official Documentation**: https://docs.python.org/3/
- 💬 **Python Community**: Stack Overflow, Reddit's r/learnprogramming
- 🐛 **Debug Issues**: Use `print()` statements and Python's `pdb` debugger

---

## 👥 Using This Repository

### **For Learners**
1. Work through modules sequentially
2. Complete all practice problems before moving forward
3. Refer to cheatsheets and interview questions for review
4. Build the mini-projects to reinforce learning
5. Tackle the final project to demonstrate mastery

### **For Instructors**
- Use this structured curriculum for Python foundation courses
- Adapt projects and exercises based on student level
- Leverage interview questions for assessment

---

## 📋 Quick Navigation

```
module_1_programming_foundations/
├── 01_intro_python/              # Python basics
├── 02_operators_conditionals/    # Logic and decision-making
├── 03_loops_iterations/          # Repetition and patterns
├── 04_functions/                 # Reusable code blocks
├── 05_strings_lists_tuples/      # Sequence data types
├── 06_dicts_sets_algorithms/     # Advanced data structures
├── 07_files_exceptions/          # I/O and error handling
├── 08_oop/                       # Object-oriented basics
├── 09_advanced_oop/              # Inheritance & polymorphism
├── 10_modules_packages/          # Code organization
├── mini_projects/                # Small focused projects
├── final_project/                # Capstone application
└── README.md                     # This file
```

---

## 🚀 Next Steps

1. **Get Set Up**: Install Python and clone the repository
2. **Start Learning**: Begin with Module 01
3. **Practice Consistently**: Complete exercises and practice problems
4. **Build Projects**: Apply knowledge through mini and final projects
5. **Review & Reflect**: Use cheatsheets and interview questions to solidify concepts
6. **Level Up**: Explore advanced topics like async programming, testing frameworks, or web development

---

## 📝 License

This educational material is provided for learning purposes. Refer to the LICENSE file for details.

---

## 🙌 Contributing

Found an issue? Have a suggestion? Contributions are welcome!
- Report issues with clear descriptions
- Suggest improvements to existing code or explanations
- Add additional practice problems or mini-projects
- Help make this resource better for other learners

---

## Author

Created and maintained by **Atharva Shirodkar**  
GitHub: [@atharvashirodkar](https://github.com/atharvashirodkar)

Maintained the Python Programming Foundation learning repository.

---

**Happy Learning! 🎓**

*Start with the basics, practice consistently, and you'll master Python programming in no time.*

