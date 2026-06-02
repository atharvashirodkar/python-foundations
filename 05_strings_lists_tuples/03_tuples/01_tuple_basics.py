# Creating tuples

numbers = (10, 20, 30, 40)

print(numbers)

# Creating Empty tuple

num = ()

print(type(num))


# Tuple with different data types

student = ("Rahul", 21, "Mumbai")

print(student)


# Accessing tuple elements

print(student[0])
print(student[1])


# Negative indexing

print(student[-1])


# Tuple length

print(len(student))


# Loop through tuple

for item in numbers:
    print(item)


# Tuple concatenation

tuple1 = (1, 2)
tuple2 = (3, 4)

result = tuple1 + tuple2

print(result)


# Repeating tuple values

values = ("Python",) * 3

print(values)