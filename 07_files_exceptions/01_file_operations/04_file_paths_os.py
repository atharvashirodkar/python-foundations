# File Paths and OS Module in Python

import os

# ---------------------------------------------------
# Current Working Directory
# ---------------------------------------------------

current_directory = os.getcwd()

print("Current Working Directory:")
print(current_directory)

# ---------------------------------------------------
# Relative Path
# ---------------------------------------------------

# Relative path means:
# File path relative to the current project folder

# with open("data/students.txt", "r") as file:
#     print(file.read())

# ---------------------------------------------------
# Absolute Path
# ---------------------------------------------------

# Absolute path means:
# Complete path of a file from the root directory

# Example:
# C:/Users/Deepak/Desktop/project/data/students.txt

# ---------------------------------------------------
# Checking if a file exists
# ---------------------------------------------------

if os.path.exists("data/students.txt"):
    print("File exists")

else:
    print("File does not exist")

# ---------------------------------------------------
# Creating a new folder
# ---------------------------------------------------

if not os.path.exists("backup"):
    os.mkdir("backup")
    
    print("Folder created successfully")

    with open("backup/students_backup.txt", "w") as backup:
        with open("data/students.txt", "r") as students:
            
            data = students.readline()
            while data != "":
                print(data)
                backup.write(data)
                data = students.readline()
            print("Data Backup succesfully")
            
            print("File created")
        
else:
    print("Folder already exists")
    with open("backup/students_backup.txt", "w") as backup:
        with open("data/students.txt", "r") as students:

            data = students.readline()
            while data != "":
                print(data)
                backup.write(data)
                data = students.readline()
            print("Data Backup succesfully")


# ---------------------------------------------------
# Important Notes
# ---------------------------------------------------

# os.getcwd()
# Returns current working directory

# os.path.exists()
# Checks whether a file or folder exists

# os.mkdir()
# Creates a new folder

# Relative Path
# Easier and commonly used in projects

# Absolute Path
# Full system path of a file or folder