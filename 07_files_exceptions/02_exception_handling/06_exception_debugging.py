# --------------------------------------------
# Exception Debugging
# --------------------------------------------
# Debugging means finding and fixing errors
# in a program.
#
# Python provides traceback messages that help
# identify:
# - error type
# - error location
# - error cause
# --------------------------------------------


# ============================================
# Example 1: Reading Error Messages
# ============================================

print("Example 1: Reading Error Messages")

try:
    number = int("hello")

except ValueError as error:
    print("Error Type:", type(error))
    print("Error Message:", error)

print()


# ============================================
# Example 2: Finding Line Numbers
# ============================================

print("Example 2: Line Number Debugging")


def divide_numbers(a, b):
    return a / b


try:
    result = divide_numbers(10, 0)

    print(result)

except ZeroDivisionError as error:
    print("Error occurred:", error)
    traceback.print_exc()

print()


# ============================================
# Example 3: Debugging List Errors
# ============================================

print("Example 3: List Index Debugging")

numbers = [10, 20, 30]

try:
    print(numbers[5])

except IndexError as error:
    print("Index Error:", error)
    print("Valid indexes are 0 to", len(numbers) - 1)

print()


# ============================================
# Example 4: Debugging Dictionary Errors
# ============================================

print("Example 4: Dictionary Key Debugging")

student = {
    "name": "Aman",
    "age": 21
}

try:
    print(student["course"])

except KeyError as error:
    print("Key Error:", error)
    print("Available keys:", student.keys())

print()


# ============================================
# Example 5: Using traceback Module
# ============================================

print("Example 5: traceback Module")

import traceback

try:
    result = 50 / 0

except ZeroDivisionError:
    print("Detailed Traceback:")

    traceback.print_exc()

print()


# ============================================
# Example 6: Debugging File Errors
# ============================================

print("Example 6: File Debugging")

try:
    with open("data/missing_file.txt", "r") as file:
        content = file.read()

except FileNotFoundError as error:
    print("File Error:", error)
    print("Check whether the file exists in the data folder.")

print()


# ============================================
# Common Debugging Tips
# ============================================

# 1. Read error messages carefully
# 2. Check line numbers in traceback
# 3. Print variable values when debugging
# 4. Handle specific exceptions
# 5. Use meaningful variable names
# 6. Test with different inputs
# 7. Do not ignore exceptions silently


# ============================================
# Bad Practice Example
# ============================================

# Avoid this:

# try:
#     risky_code()
# except:
#     pass

# This hides errors and makes debugging difficult.
