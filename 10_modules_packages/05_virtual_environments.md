# Virtual Environments in Python

## What is a Virtual Environment?

A virtual environment is an isolated Python environment for a project.

It allows each project to have:
- separate packages
- separate dependencies
- cleaner project setup

Without virtual environments, packages install globally and can create version conflicts.

---

# Why Use Virtual Environments?

Example:

Project A needs:
```text
django==4.2
```

Project B needs:
```text
django==5.0
```

Installing both globally can cause conflicts.

Virtual environments solve this problem.

---

# Creating a Virtual Environment

## Windows

```bash
python -m venv venv
```

## Mac/Linux

```bash
python3 -m venv venv
```

This creates a folder named:

```text
venv/
```

---

# Activating Virtual Environment

## Windows

```bash
venv\Scripts\activate
```

## Mac/Linux

```bash
source venv/bin/activate
```

After activation, you may see:

```text
(venv)
```

in the terminal.

---

# Installing Packages

Example:

```bash
pip install requests
```

Check installed packages:

```bash
pip list
```

---

# requirements.txt

Save installed packages:

```bash
pip freeze > requirements.txt
```

Install packages from file:

```bash
pip install -r requirements.txt
```

---

# Deactivating Environment

```bash
deactivate
```

---

# Common Folder Structure

```text
project/
│
├── venv/
├── main.py
├── requirements.txt
└── README.md
```

---

# Important Notes

- Do not manually edit the `venv/` folder
- Usually `venv/` is added to `.gitignore`
- Every major Python project should use a virtual environment
- `pip` is Python's package manager

---

# Common Beginner Mistakes

## 1. Forgetting to activate venv

Packages install globally instead.

---

## 2. Uploading venv folder to GitHub

Bad practice.

Use `.gitignore`.

---

## 3. Confusing Python installation with virtual environment

A virtual environment does NOT install Python again.
It creates an isolated environment using the existing Python installation.