"""
Problem Statement:
Write a Python program to count the frequency of each character
in a given string entered by the user.

Example:
Input: apple
Output:
a -> 1
p -> 2
l -> 1
e -> 1
"""

char = input("Enter a string: ")

# Method 1:

bucket = []
for i in char:
    if i in bucket:
        continue
    count = char.count(i)
    print(f'{i} -> {count}')
    bucket.append(i)


# Method 2:
str_lower = list(char.lower())

characters = []

for i in str_lower:
    if i in characters:
        continue
    else:
        characters.append(i)
        count = str_lower.count(i)
        print(f'{i} -> {count}')