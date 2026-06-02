# Tuple unpacking

student = ("Rahul", 21, "Mumbai")

name, age, city = student

print(name)
print(age)
print(city)


# Unpacking numbers

numbers = (10, 20, 30)

a, b, c = numbers

print(a)
print(b)
print(c)


# Swapping values

x = 5
y = 10

x, y = y, x

print(x)
print(y)


# Using * for multiple values

values = (1, 2, 3, 4, 5)

first, *middle, last = values

print(first)
print(middle)
print(last)


# Ignoring values

data = ("Python", 3.12, "Programming")

language, _, category = data

print(language)
print(category)


# Loop with tuple unpacking

students = [
    ("Rahul", 85),
    ("Aman", 90),
    ("Priya", 88)
]

for name, marks in students:
    print(name, marks)
