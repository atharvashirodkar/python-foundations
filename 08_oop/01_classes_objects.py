"""
Topic: Classes and Objects in Python

A class is a blueprint for creating objects.
An object is an instance of a class.
"""


# Creating a class
class Student:
    pass


# Creating objects
student1 = Student()
student2 = Student()

print("student1:", student1)
print("student2:", student2)

print("\nType of student1:", type(student1))


# --------------------------------------------------
# Class with attributes
# --------------------------------------------------

class Car:
    brand = "Toyota"
    color = "White"


car1 = Car()
car2 = Car()

print("\nCar 1 Brand:", car1.brand)
print("Car 1 Color:", car1.color)

print("Car 2 Brand:", car2.brand)
print("Car 2 Color:", car2.color)


# --------------------------------------------------
# Modifying object attributes
# --------------------------------------------------

car1.brand = "Honda"
car1.color = "Black"

print("\nAfter Modification:")
print("Car 1 Brand:", car1.brand)
print("Car 1 Color:", car1.color)

print("Car 2 Brand:", car2.brand)
print("Car 2 Color:", car2.color)


# --------------------------------------------------
# Real-world Example
# --------------------------------------------------

class Employee:
    company = "ABC Technologies"
    department = "Software Development"


emp1 = Employee()
emp2 = Employee()

emp1.name = "Rahul"
emp1.salary = 50000

emp2.name = "Priya"
emp2.salary = 60000

print("\nEmployee Details")
print("----------------")
print("Name:", emp1.name)
print("Salary:", emp1.salary)
print("Company:", emp1.company)

print()

print("Name:", emp2.name)
print("Salary:", emp2.salary)
print("Company:", emp2.company)