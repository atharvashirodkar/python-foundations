# =========================================
# USING CUSTOM MODULES
# =========================================

# Suppose we have another file:
#
# calculator.py
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# -----------------------------------------

# Importing the entire module
import calculator

print("Addition:", calculator.add(10, 5))
print("Subtraction:", calculator.subtract(10, 5))


# -----------------------------------------

# Importing specific functions
from calculator import add

print("Add Function:", add(20, 30))


# -----------------------------------------

# Using aliases
import calculator as calc

print("Alias Example:", calc.add(100, 50))


# =========================================
# WHY CUSTOM MODULES?
# =========================================

"""
Benefits of Custom Modules:

1. Better code organization
2. Code reusability
3. Easier debugging
4. Cleaner projects
5. Separation of concerns

Instead of writing everything
in one file, we split logic
into multiple modules.
"""