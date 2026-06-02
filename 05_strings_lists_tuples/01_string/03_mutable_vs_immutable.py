# 04_mutable_vs_immutable.py

# Immutable Example (String)

name = "Python"

print("Before:", name)
print("Address:", id(name))

name = name + " Language"

print("After :", name)
print("Address:", id(name))


print("\n------------------\n")


# Mutable Example (List)

numbers = [1, 2, 3]

print("Before:", numbers)
print("Address:", id(numbers))

numbers.append(4)

print("After :", numbers)
print("Address:", id(numbers))