# Modules & Packages Practice Questions

## Question 1 — Basic Module Import

Create a file named:

```text
operations.py
```

Inside it, create the following functions:

- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

Now create another file:

```text
main.py
```

Import the functions and perform all operations using user input.

---

## Question 2 — Import Entire Module vs Specific Functions

Using the same `operations.py` file:

### Part A

Import the entire module:

```python
import operations
```

Call:
- operations.add()
- operations.subtract()

### Part B

Import specific functions:

```python
from operations import add, subtract
```

Call the functions directly.

### Task

Write the difference between:
- importing the entire module
- importing specific functions

---

## Question 3 — Using Aliases

Create a module named:

```text
message_utils.py
```

Add:
- welcome_message(name)
- goodbye_message(name)

Import the module using an alias:

```python
import message_utils as msg
```

Call both functions using the alias.

---

## Question 4 — Exploring Built-in Modules

Use the following built-in modules:

- math
- random
- datetime

Perform these tasks:

### math
- Find square root of 64
- Find value of 2 raised to power 5

### random
- Generate a random number between 1 and 100
- Randomly select a fruit from a list

### datetime
- Print current date and time

---

## Question 5 — Create Your Own Package

Create the following structure:

```text
mypackage/
│
├── __init__.py
├── math_utils.py
└── string_utils.py
```

### math_utils.py

Create:
- square(num)
- cube(num)

### string_utils.py

Create:
- to_upper(text)
- reverse_text(text)

Import and use all functions inside `main.py`.

---

## Question 6 — Understanding __name__

Create a file:

```text
main_dunder.py
```

Print:

```python
print(__name__)
```

Add:

```python
if __name__ == "__main__":
    print("Running Directly")
```

Now:

### Step 1
Run the file directly.

### Step 2
Import it inside another file.

### Task

Observe:
- how `__name__` changes
- which code executes during import

Write your observations.

---

## Question 7 — Invalid Module Names

Create a file:

```text
01_utils.py
```

Try importing it:

```python
import 01_utils
```

### Task

Observe the error.

Answer:
- Why does the import fail?
- What are valid Python module naming rules?

---

## Question 8 — Mini Modular Calculator

Create the following structure:

```text
calculator_app/
│
├── main.py
├── basic_operations.py
└── advanced_operations.py
```

### basic_operations.py

Create:
- add()
- subtract()
- multiply()
- divide()

### advanced_operations.py

Create:
- square()
- factorial()

### main.py

Import all functions and create a menu-driven calculator program.

---

## Question 9 — Module Execution Experiment

Create a file:

```text
demo_module.py
```

Add:
- a print statement at the top level
- one function
- one `if __name__ == "__main__"` block

Now import the module into another file.

### Task

Identify:
- which lines execute immediately
- which lines execute only during direct execution

Explain why this happens.

---

## Question 10 — Real-World Thinking

Answer the following:

1. Why do large Python projects use modules and packages?
2. What problems occur if all code is written in one file?
3. Why are virtual environments important?
4. Why should `venv/` usually not be uploaded to GitHub?