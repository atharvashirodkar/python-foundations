# Nested dictionary stores dictionaries inside another dictionary

# Real-world example: 
# student database
students = {
    101: {
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    },

    102: {
        "name": "Anjali",
        "age": 22,
        "course": "Data Science"
    }
}

print("\n--- Student Database ---")
print(students)

# Access nested dictionary values
print("\n--- Accessing Student Details ---")

print("Student ID 101 Name :", students[101]["name"])
print("Student ID 102 Course :", students[102]["course"])

# Add new student
students[103] = {
    "name": "Aman",
    "age": 20,
    "course": "Web Development"
}

print("\n--- After Adding New Student ---")
print(students)

# Update nested value
students[101]["age"] = 23

print("\n--- After Updating Age ---")
print(students)

# Remove a student
students.pop(102)

print("\n--- After Removing Student 102 ---")
print(students)

# Loop through nested dictionary
print("\n--- Looping Through Students ---")

for student_id, details in students.items():
    print(f"\nStudent ID : {student_id}")

    for key, value in details.items():
        print(f"{key} : {value}")

# Check if student exists
print("\n--- Checking Student ID ---")

if 101 in students:
    print("Student 101 exists")

# Total number of students
print("\n--- Total Students ---")
print(len(students))