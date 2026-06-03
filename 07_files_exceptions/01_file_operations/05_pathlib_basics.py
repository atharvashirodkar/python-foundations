# Pathlib in Python

# pathlib provides an easier and cleaner
# way to work with files and folders

from pathlib import Path

# ---------------------------------------------------
# Creating a Path object
# ---------------------------------------------------

file_path = Path("data/students.txt")

print(file_path)

# ---------------------------------------------------
# Checking if file exists
# ---------------------------------------------------

if file_path.exists():
    print("File exists")

else:
    print("File does not exist")

# ---------------------------------------------------
# Reading file content
# ---------------------------------------------------

content = file_path.read_text()

print(f"Content: {content}")
print("====================")

# ---------------------------------------------------
# Writing to a file
# ---------------------------------------------------

new_file = Path("data/pathlib_demo.txt")

new_file.write_text("Deepak\nKhushi\nHarold\n")

print("Data written successfully")

# ---------------------------------------------------
# Appending data to a file
# ---------------------------------------------------

with open(new_file, "a") as file:
    file.write("Tripti\n")

print("New data appended successfully")

# ---------------------------------------------------
# Reading updated content
# ---------------------------------------------------

updated_content = new_file.read_text()

print(updated_content)

# ---------------------------------------------------
# Important Notes
# ---------------------------------------------------

# Path()
# Creates a file path object

# exists()
# Checks whether file exists or not

# read_text()
# Reads complete file content

# write_text()
# Writes data into a file

# pathlib makes file handling cleaner
# and easier compared to traditional methods