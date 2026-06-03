# --------------------------------------------
# Custom Exceptions
# --------------------------------------------
# Python allows us to create our own exception
# classes for specific application errors.
#
# Custom exceptions improve:
# - readability
# - debugging
# - error organization
# --------------------------------------------


# ============================================
# Example 1: Simple Custom Exception
# ============================================

print("Example 1: Simple Custom Exception")


class InvalidAgeError(Exception):
    pass


try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")

    print("Access granted.")

except InvalidAgeError as error:
    print("Custom Exception:", error)

print()


# ============================================
# Example 2: Custom Exception in Function
# ============================================

print("Example 2: Function Validation")


class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Withdrawal amount exceeds balance."
        )

    return balance - amount


try:
    remaining_balance = withdraw(3000, 5000)

    print("Remaining Balance:", remaining_balance)

except InsufficientBalanceError as error:
    print("Transaction Failed:", error)

print()


# ============================================
# Example 3: Student Marks Validation
# ============================================

print("Example 3: Marks Validation")


class InvalidMarksError(Exception):
    pass


try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError(
            "Marks must be between 0 and 100."
        )

    print("Marks accepted.")

except InvalidMarksError as error:
    print("Error:", error)

print()


# ============================================
# Example 4: Password Validation
# ============================================

print("Example 4: Password Validation")


class WeakPasswordError(Exception):
    pass


def validate_password(password):

    if len(password) < 8:
        raise WeakPasswordError(
            "Password must contain at least 8 characters."
        )

    print("Password is strong.")


try:
    user_password = input("Enter password: ")

    validate_password(user_password)

except WeakPasswordError as error:
    print("Validation Error:", error)

print()


# ============================================
# Example 5: Multiple Custom Exceptions
# ============================================

print("Example 5: Multiple Custom Exceptions")


class InvalidUsernameError(Exception):
    pass


class InvalidPasswordError(Exception):
    pass


try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != "admin":
        raise InvalidUsernameError("Incorrect username.")

    if password != "admin123":
        raise InvalidPasswordError("Incorrect password.")

    print("Login successful.")

except InvalidUsernameError as error:
    print("Username Error:", error)

except InvalidPasswordError as error:
    print("Password Error:", error)

print()


# ============================================
# Important Notes
# ============================================

# 1. Custom exceptions inherit from Exception
# 2. Use meaningful exception names
# 3. Custom exceptions improve code clarity
# 4. Useful for large applications
# 5. Avoid creating unnecessary exceptions