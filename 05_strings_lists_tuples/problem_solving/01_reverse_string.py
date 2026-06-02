
# Problem Statement:
# Write a Python program that takes a string input from the user
# and prints the reversed version of that string.
#
# Example:
# Input: hello
# Output: olleh

user = input("Enter a string: ")

# method 1:
rev = user[::-1]
print(rev)


# method 2:
rev = ""
for i in range(len(user)-1, -1, -1):
    rev = rev + user[i]
print(rev)


# method 3: (improved version of method 2)
rev = []
for i in range(len(user)-1, -1, -1):
    rev.append(user[i])
print("".join(rev))