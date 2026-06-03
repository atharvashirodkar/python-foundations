# Working with JSON Files in Python

# JSON
# JavaScript Object Notation

# JSON stores data in key-value format

# ---------------------------------------------------
# Example JSON Data
# ---------------------------------------------------

# {
#     "name": "Khushi",
#     "college": "Masai",
#     "marks": 90,
#     "attendance": 94.5,
#     "city": "Delhi"
# }

import json

# ---------------------------------------------------
# Python Dictionary
# ---------------------------------------------------

student = {
    "name": "Pawan",
    "college": "MIT",
    "marks": 89,
    "attendance": 97.5,
    "city": "Pune"
}

print(student)

# ---------------------------------------------------
# Writing JSON data into a file
# ---------------------------------------------------

with open("data/student.json", "w") as file:
    json.dump(student, file)

print("JSON data written successfully")

# ---------------------------------------------------
# Reading JSON data from a file
# ---------------------------------------------------

with open("data/student.json", "r") as file:
    file_content = json.load(file)

print(file_content)

# ---------------------------------------------------
# Accessing JSON values
# ---------------------------------------------------

print(file_content["name"])
print(file_content["marks"])
print(file_content["city"])

# ---------------------------------------------------
# Important Notes
# ---------------------------------------------------

# json.dump()
# Writes Python data into JSON file

# json.load()
# Reads JSON data from a file

# JSON stores data in key-value format

# JSON is commonly used in:
# APIs
# Web applications
# Configuration files
# Data storage