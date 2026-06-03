# Writing and Appending Files in Python

# ---------------------------------------------------
# Writing to a file using 'w' mode
# ---------------------------------------------------

with open("data/students.txt", "w") as file:
    file.write("Deepak\n")
    file.write("Khushi\n")
    file.write("Harold\n")

print("Data written successfully")

# ---------------------------------------------------
# Reading the updated file
# ---------------------------------------------------

with open("data/students.txt", "r") as file:
    content = file.read()

    print(content)

# ---------------------------------------------------
# Appending data using 'a' mode
# ---------------------------------------------------

with open("data/students.txt", "a") as file:
    file.write("Tripti\n")
    file.write("Sagarika\n")

print("New data appended successfully")

# ---------------------------------------------------
# Reading the file again
# ---------------------------------------------------

with open("data/students.txt", "r") as file:
    content = file.read()

    print(content)

# ---------------------------------------------------
# Difference between 'w' and 'a'
# ---------------------------------------------------

# 'w' mode
# Deletes old content and writes new content

# 'a' mode
# Keeps old content and adds new content at the end

# ---------------------------------------------------
# Creating a new file automatically
# ---------------------------------------------------

with open("data/names.txt", "w") as file:
    file.write("Aman\n")
    file.write("Ritika\n")

print("New file created successfully")

# ---------------------------------------------------
# Important Notes
# ---------------------------------------------------

# If the file does not exist:
# 'w' mode creates the file automatically

# Use 'w' carefully because old data gets deleted

# Use 'a' when you want to keep existing data