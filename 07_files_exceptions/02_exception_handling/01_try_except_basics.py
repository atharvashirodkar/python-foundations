# ============================================
# 01_try_except_basics.py
# ============================================

# --------------------------------------------
# What is Exception Handling?
# --------------------------------------------
# Exceptions are runtime errors that can crash
# a program if not handled properly.
#
# try:
#     Code that may cause an error
#
# except:
#     Code that runs if error occurs
# --------------------------------------------


# ============================================
# Example 1: Division by Zero
# ============================================

print("Example 1: Division by Zero")

try:
    number = 10
    result = number / 0
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print()


# ============================================
# Example 2: Invalid Input
# ============================================

print("Example 2: Invalid Input")

try:
    age = int(input("Enter your age: "))
    print("Your age is:", age)

except ValueError:
    print("Error: Please enter a valid number.")

print()


# ============================================
# Example 3: Multiple Statements Inside try
# ============================================

print("Example 3: Multiple Statements")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Division Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid numeric input.")

print()


# ============================================
# Example 4: Program Continues After Exception
# ============================================

print("Example 4: Program Continues")

try:
    value = int("hello")

except ValueError:
    print("Conversion failed.")

print("Program is still running successfully.")

print()


# ============================================
# Example 5: Generic Exception (Not Recommended)
# ============================================

print("Example 5: Generic Exception")

try:
    numbers = [1, 2, 3]
    print(numbers[10])

except Exception as error:
    print("An error occurred.")
    print("Error message:", error)

print()


# ============================================
# Best Practices
# ============================================

# 1. Catch specific exceptions whenever possible
# 2. Avoid using bare except:
# 3. Keep try blocks small
# 4. Use exceptions to prevent program crashes
# 5. Read error messages carefully
