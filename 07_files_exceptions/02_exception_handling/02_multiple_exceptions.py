# ============================================
# 02_multiple_exceptions.py
# ============================================

# --------------------------------------------
# Multiple Exception Handling
# --------------------------------------------
# A program can produce different types of
# errors. We can handle each error separately
# using multiple except blocks.
# --------------------------------------------


# ============================================
# Example 1: Handling Different Exceptions
# ============================================

print("Example 1: Different Exceptions")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print()


# ============================================
# Example 2: File Handling Exception
# ============================================

print("Example 2: File Exception")

try:
    file = open("data/sample.txt", "r")
    content = file.read()

    print(content)

    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

print()


# ============================================
# Example 3: Index Error
# ============================================

print("Example 3: Index Error")

try:
    numbers = [10, 20, 30]

    index = int(input("Enter list index: "))

    print("Value:", numbers[index])

except ValueError:
    print("Error: Index must be a number.")

except IndexError:
    print("Error: Index out of range.")

print()


# ============================================
# Example 4: Multiple Exceptions in One Block
# ============================================

print("Example 4: Multiple Exceptions Together")

try:
    value = int(input("Enter a number: "))
    result = 100 / value

    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Error: Invalid input or division by zero.")

print()


# ============================================
# Example 5: Generic Exception at the End
# ============================================

print("Example 5: Generic Exception")

try:
    dictionary = {
        "name": "Rahul",
        "age": 21
    }

    print(dictionary["city"])

except KeyError:
    print("Error: Key not found in dictionary.")

except Exception as error:
    print("Unexpected error occurred.")
    print("Error:", error)

print()


# ============================================
# Important Notes
# ============================================

# 1. Specific exceptions should come first
# 2. Generic Exception should come last
# 3. One try block can have multiple except blocks
# 4. Multiple exceptions can be grouped together
# 5. Proper exception handling improves program stability