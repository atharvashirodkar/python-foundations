# Using + operator

first_name = "Rahul"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)


# Using format()

course = "Python"
duration = 3

print("I am learning {} for {} months.".format(course, duration))


# Using f-string

name = "Aman"
age = 21

print(f"My name is {name} and I am {age} years old.")


# Expressions inside f-string

num1 = 10
num2 = 20

print(f"Addition: {num1 + num2}")


# Float formatting

pi = 3.14159265359

print(f"Pi value: {pi:.2f}")


# Text alignment

word = "Python"

print(f"{word:<10} Left")
print(f"{word:^10} Center")
print(f"{word:>10} Right")


# Padding numbers

student_id = 7

print(f"Student ID: {student_id:03}")