# --------------------------------------------
# else and finally in Exception Handling
# --------------------------------------------
#
# else:
#     Runs only if no exception occurs
#
# finally:
#     Runs no matter what happens
# --------------------------------------------


# ============================================
# Example 1: Using else Block
# ============================================

print("Example 1: else Block")

try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Error: Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Division Result:", result)
    print("No exception occurred.")

print()


# ============================================
# Example 2: Using finally Block
# ============================================

print("Example 2: finally Block")

try:
    file = open("data/sample.txt", "r")

    content = file.read()

    print(content)

except FileNotFoundError:
    print("Error: File not found.")

finally:
    print("File operation completed.")

print()


# ============================================
# Example 3: finally Always Executes
# ============================================

print("Example 3: finally Always Runs")

try:
    number = int(input("Enter a number: "))

    result = 50 / number

    print("Result:", result)

except Exception as error:
    print("Error:", error)

finally:
    print("This block always executes.")

print()


# ============================================
# Example 4: Combining try, except, else, finally
# ============================================

print("Example 4: Full Structure")

try:
    marks = int(input("Enter marks: "))

except ValueError:
    print("Invalid input.")

else:
    print("Marks entered successfully.")
    print("Marks:", marks)

finally:
    print("Program execution completed.")

print()


# ============================================
# Example 5: Closing Files Safely
# ============================================

print("Example 5: Safe File Closing")

file = None

try:
    file = open("data/sample.txt", "r")

    print(file.read())

except FileNotFoundError:
    print("Error: File not found.")

finally:
    if file:
        file.close()
        print("File closed successfully.")

print()


# ============================================
# Important Notes
# ============================================

# else block:
# - Runs only when no exception occurs
#
# finally block:
# - Always runs
# - Commonly used for cleanup
# - Useful for closing files/database connections
#
# Order:
# try -> except -> else -> finally