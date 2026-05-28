'''
Python match-case Statement

Topics Covered:
- match-case Syntax
- Multiple Cases
- Default Case
'''


# =========================================
# Basic match-case Example
# =========================================

print("===== match-case Statement =====")

day = 3

match day:
    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case _:
        print("Invalid Day")


# =========================================
# User Input Example
# =========================================

print("\n===== Calculator Operation =====")

choice = input("Enter operation (+, -, *, /): ")

num1 = 10
num2 = 5

match choice:
    case "+":
        print("Result:", num1 + num2)

    case "-":
        print("Result:", num1 - num2)

    case "*":
        print("Result:", num1 * num2)

    case "/":
        print("Result:", num1 / num2)

    case _:
        print("Invalid Operation")