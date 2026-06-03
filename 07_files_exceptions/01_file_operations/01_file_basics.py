# File Handling in Python
# Working with files using Python programs

# ---------------------------------------------------
# Use Case:
# Student Management System
#
# Student details:
# name, email, password, phone number,
# address, attendance, marks etc.
# ---------------------------------------------------

# Opening a file using open()

# Syntax:
# open("filename", "mode")

# Common Modes:
# r -> Read
# w -> Write
# a -> Append
# x -> Create

# ---------------------------------------------------
# Opening a file in read mode
# ---------------------------------------------------

file = open("data/students.txt", "r")

print(file)

file.close()

# ---------------------------------------------------
# Why closing a file is important?
# ---------------------------------------------------

# 1. Frees system resources
# 2. Prevents file corruption
# 3. Avoids memory leaks
# 4. Good programming practice

# ---------------------------------------------------
# Reading file content
# ---------------------------------------------------

file = open("data/students.txt", "r")

content = file.read()

print(content)

file.close()

# ---------------------------------------------------
# Using 'with open()'
# Python automatically closes the file
# ---------------------------------------------------

with open("data/students.txt", "r") as file:
    content = file.read()

    print(content)

# No need to manually close the file

# ---------------------------------------------------
# Opening a file in write mode
# ---------------------------------------------------

with open("data/sample.txt", "w") as file:
    file.write("Kalpesh\n")
    file.write("Sagarika\n")

print("Data written successfully")

# ---------------------------------------------------
# Important Notes
# ---------------------------------------------------

# 'w' mode:
# Deletes old content and writes new content

# 'a' mode:
# Keeps old content and adds new content at the end

# If file doesn't exist:
# 'w' mode creates a new file automatically

# Always remember:
# Use with open() whenever possible