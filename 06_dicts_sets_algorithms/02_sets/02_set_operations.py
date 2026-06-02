# Set operations example

# Students enrolled in Python course
python_students = {"Rahul", "Anjali", "Aman", "Priya"}

# Students enrolled in Data Science course
data_science_students = {"Aman", "Priya", "Karan", "Neha"}

print("\n--- Python Students ---")
print(python_students)

print("\n--- Data Science Students ---")
print(data_science_students)

# union() combines all unique values
print("\n--- Union ---")

all_students = python_students.union(data_science_students)

print(all_students)

# intersection() returns common values
print("\n--- Intersection ---")

common_students = python_students.intersection(data_science_students)

print(common_students)

# difference() returns unique values from first set
print("\n--- Difference ---")

only_python = python_students.difference(data_science_students)

print(only_python)

# symmetric_difference() returns non-common values
print("\n--- Symmetric Difference ---")

unique_students = python_students.symmetric_difference(data_science_students)

print(unique_students)

# Check subset
print("\n--- Subset Check ---")

weekend_batch = {"Rahul", "Aman"}

print(weekend_batch.issubset(python_students))

# Check superset
print("\n--- Superset Check ---")

print(python_students.issuperset(weekend_batch))