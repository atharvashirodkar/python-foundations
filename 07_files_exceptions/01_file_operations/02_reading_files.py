# Reading Files in Python

# ---------------------------------------------------
# read()
# Reads complete file content
# ---------------------------------------------------

with open("data/students.txt", "r") as file:
    content = file.read()

    print(content)

# ---------------------------------------------------
# readline()
# Reads one line at a time
# ---------------------------------------------------

with open("data/students.txt", "r") as file:

    first_line = file.readline()
    print(first_line)

    second_line = file.readline()
    print(second_line)

# ---------------------------------------------------
# readlines()
# Returns all lines as a list
# ---------------------------------------------------

with open("data/students.txt", "r") as file:

    lines = file.readlines()

    print("lines:", lines)

# ---------------------------------------------------
# Looping through a file
# ---------------------------------------------------

with open("data/students.txt", "r") as file:

    for line in file:
        print(line)

# ---------------------------------------------------
# strip()
# Removes extra spaces and newline characters
# ---------------------------------------------------

with open("data/students.txt", "r") as file:

    for line in file:
        print(line.strip())

# ---------------------------------------------------
# Example Output
# ---------------------------------------------------

# Deepak
# Khushi
# Harold
# Tripti

# ---------------------------------------------------
# Important Notes
# ---------------------------------------------------

# read()
# Reads the entire file

# readline()
# Reads one line at a time

# readlines()
# Returns all lines in list format

# strip()
# Removes extra spaces and \n characters