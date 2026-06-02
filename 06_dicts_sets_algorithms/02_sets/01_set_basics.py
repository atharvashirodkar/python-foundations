# Set stores unique values

# Real-world example: registered course students
students = {"Rahul", "Anjali", "Aman", "Rahul"}

print("\n--- Student Set ---")
print(students)

# Duplicate values are removed automatically
print("\n--- Unique Students ---")
print(students)

# Add new value
students.add("Priya")

print("\n--- After Adding Student ---")
print(students)

# Remove a value
students.remove("Aman")

print("\n--- After Removing Student ---")
print(students)

# discard() avoids error if value does not exist
students.discard("Karan")

print("\n--- After Using discard() ---")
print(students)

# Check if value exists
print("\n--- Checking Student ---")

if "Rahul" in students:
    print("Rahul is registered")

# Loop through set
print("\n--- Looping Through Set ---")

for student in students:
    print(student)

# Length of set
print("\n--- Total Students ---")
print(len(students))