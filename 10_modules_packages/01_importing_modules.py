# =========================================
# IMPORTING BUILT-IN MODULES IN PYTHON
# =========================================

# Importing the entire module
import math

print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))


# -----------------------------------------

# Importing specific functions
from random import randint, choice

print("Random Number:", randint(1, 10))

fruits = ["apple", "banana", "mango"]
print("Random Fruit:", choice(fruits))


# -----------------------------------------

# Using aliases
import datetime as dt

current_time = dt.datetime.now()
print("Current Time:", current_time)


# -----------------------------------------

# Importing everything (not recommended)
from math import *

print("Pi Value:", pi)
print("Factorial:", factorial(5))


# =========================================
# NOTES
# =========================================

"""
1. import module_name
   -> Imports the entire module

2. from module import function
   -> Imports specific functions

3. import module as alias
   -> Gives a shorter alias name

4. from module import *
   -> Imports everything (avoid in real projects)

Common Built-in Modules:
- math
- random
- datetime
- os
- pathlib
"""