# Lists are ordered collections – 
# fundamental data structures for managing groups of related data efficiently.

# Without lists - managing 1000 items is a nightmare
# student1 = "Alice"
# student2 = "Bob"
# ...

# With lists - elegant for any size!
students = ["Alice", "Bob", "Charlie"] # Can hold millions!

# Creating Empty Lists

# Method 1: Square brackets (preferred)
empty = []

# Method 2: list() constructor
empty = list()

even_nums = list(range(0,10,2))

odd_nums = list(range(1,10,2))

print(even_nums)
print(odd_nums)

chars = list("hello")      # ['h', 'e', 'l', 'l', 'o']
words = "a b c".split()     # ['a', 'b', 'c']
items = "x,y,z".split(',') # ['x', 'y', 'z']

# Accessing list elements using loop
fruits = ["Apple", "Banana", "Mango"]

for i in fruits:
    print(i)

for i in range(len(fruits)):
    print(fruits[i])

# Methods in list

fruits.sort()
# print(fruits)

fruits.append("Apple")
print(fruits)