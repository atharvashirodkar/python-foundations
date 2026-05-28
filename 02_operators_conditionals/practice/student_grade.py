std_name = input("Enter Student Name: ")

std_marks = int(input("Enter Student Marks: "))

attendance = float(input("Enter the attendance percentage: "))

isEligible = False

if std_marks >= 90:
    grade = "Grade A"
elif std_marks >= 75:
    grade = "Grade B"
elif std_marks >= 50:
    grade = "Grade C"
else:
    grade = "Fail"

if grade != "Fail":
    if attendance > 80:
        isEligible = True

print(f"Hello {std_name}")
print(f"Grade: {grade}")
print(f"Scholarship Eligible: {isEligible}")