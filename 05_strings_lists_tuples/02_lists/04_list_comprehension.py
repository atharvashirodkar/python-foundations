# List comprehension basics

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)


# Even numbers

even_numbers = [num for num in numbers if num%2 == 0]

print(even_numbers)


# Convert names to uppercase

names = ["rahul", "aman", "priya"]

uppercase_names = [name.upper() for name in names]

print(uppercase_names)


# Length of words

words = ["python", "java", "html"]

word_lengths = [len(word) for word in words]

print(word_lengths)


# Create a list from range

values = [x for x in range(1, 6)]

print(values)