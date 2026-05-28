'''
Python Conditional Statements

Topics Covered:
- if Statement
- if-else Statement
- if-elif-else Statement
- Nested if Statement
'''


# =========================================
# if Statement
# =========================================

age = 20

print("===== if Statement =====")

if age >= 18:
    print("You are an adult.")


# =========================================
# if-else Statement
# =========================================

age = 16

print("\n===== if-else Statement =====")

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# =========================================
# if-elif-else Statement
# =========================================

marks = 82

print("\n===== if-elif-else Statement =====")

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")


# =========================================
# Nested if Statement
# =========================================

age = 20
has_id = True

print("\n===== Nested if Statement =====")

if age >= 18:
    if has_id:
        print("Entry Allowed")
    else:
        print("ID Required")
else:
    print("Underage")