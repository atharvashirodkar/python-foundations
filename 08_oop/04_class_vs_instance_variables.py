"""
Topic: Class Variables vs Instance Variables

Class Variables:
- Shared by all objects of a class
- Defined directly inside the class

Instance Variables:
- Belong to individual objects
- Defined using self inside __init__()
"""


# --------------------------------------------------
# Class Variable Example
# --------------------------------------------------

class Student:

    school = "ABC School"      # Class Variable


student1 = Student()
student2 = Student()

print("School:", student1.school)
print("School:", student2.school)


# --------------------------------------------------
# Instance Variable Example
# --------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name          # Instance Variable
        self.salary = salary      # Instance Variable


emp1 = Employee("Rahul", 50000)
emp2 = Employee("Priya", 60000)

print("\nEmployee Details")
print(emp1.name, "-", emp1.salary)
print(emp2.name, "-", emp2.salary)


# --------------------------------------------------
# Class Variable Shared by All Objects
# --------------------------------------------------

class Car:

    wheels = 4       # Class Variable

    def __init__(self, brand):
        self.brand = brand


car1 = Car("Toyota")
car2 = Car("Honda")

print("\nBefore Change")
print(car1.wheels)
print(car2.wheels)

Car.wheels = 6

print("\nAfter Change")
print(car1.wheels)
print(car2.wheels)


# --------------------------------------------------
# Instance Variables Are Independent
# --------------------------------------------------

class Laptop:

    def __init__(self, brand):
        self.brand = brand


laptop1 = Laptop("Dell")
laptop2 = Laptop("HP")

laptop1.brand = "Lenovo"

print("\nLaptop Brands")
print("Laptop 1:", laptop1.brand)
print("Laptop 2:", laptop2.brand)


# --------------------------------------------------
# Accessing Class Variables
# --------------------------------------------------

class College:

    college_name = "XYZ College"

    def __init__(self, student_name):
        self.student_name = student_name


student1 = College("Amit")

print("\nUsing Object:", student1.college_name)
print("Using Class :", College.college_name)


# --------------------------------------------------
# Counting Objects Using Class Variable
# --------------------------------------------------

class StudentCounter:

    count = 0

    def __init__(self, name):
        self.name = name
        StudentCounter.count += 1


s1 = StudentCounter("Rahul")
s2 = StudentCounter("Priya")
s3 = StudentCounter("Amit")

print("\nTotal Students:", StudentCounter.count)