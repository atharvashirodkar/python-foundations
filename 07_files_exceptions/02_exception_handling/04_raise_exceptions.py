# --------------------------------------------
# Raising Exceptions
# --------------------------------------------
# We can manually generate exceptions using
# the raise keyword.
#
# Useful for:
# - Input validation
# - Business rules
# - Preventing invalid operations
# --------------------------------------------


# ============================================
# Example 1: Raise ValueError
# ============================================

print("Example 1: Raise ValueError")

age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print("Valid age entered.")

print()


# ============================================
# Example 2: Raise Exception for Invalid Marks
# ============================================

print("Example 2: Marks Validation")

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    raise ValueError("Marks must be between 0 and 100.")

print("Marks accepted.")

print()


# ============================================
# Example 3: Raise ZeroDivisionError
# ============================================

print("Example 3: Manual ZeroDivisionError")

number = int(input("Enter a number: "))

if number == 0:
    raise ZeroDivisionError("Division by zero is not allowed.")

result = 100 / number

print("Result:", result)

print()


# ============================================
# Example 4: Using raise Inside Function
# ============================================

print("Example 4: Function Validation")


def withdraw(balance, amount):

    if amount > balance:
        raise ValueError("Insufficient balance.")

    return balance - amount


try:
    remaining_balance = withdraw(5000, 7000)

    print("Remaining Balance:", remaining_balance)

except ValueError as error:
    print("Error:", error)

print()


# ============================================
# Example 5: Re-Raising Exceptions
# ============================================

print("Example 5: Re-Raising Exception")

try:
    number = int(input("Enter a number: "))

    if number < 0:
        raise ValueError("Negative numbers are not allowed.")

except ValueError as error:
    print("Exception caught.")
    print("Error:", error)

    # Re-raise exception
    raise

print()


# ============================================
# Common Built-in Exceptions
# ============================================

# ValueError
# TypeError
# ZeroDivisionError
# FileNotFoundError
# IndexError
# KeyError


# ============================================
# Important Notes
# ============================================

# 1. raise is used to manually trigger exceptions
# 2. Useful for validating data
# 3. Helps stop invalid program execution
# 4. Exception messages should be clear
# 5. Use specific exception types whenever possible