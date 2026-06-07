"""
A package is a folder that contains
multiple Python modules.

Packages help organize large projects.
"""

# Importing from package modules
from mypackage.math_utils import add, square
from mypackage.string_utils import greet, to_upper


print("Addition:", add(10, 20))
print("Square:", square(5))

print(greet("Aman"))
print(to_upper("python"))


# =========================================
# PACKAGE STRUCTURE
# =========================================

"""
mypackage/
│
├── __init__.py
├── math_utils.py
└── string_utils.py

- __init__.py makes the folder a package
- Packages help organize related modules
- Used in real-world Python projects
"""