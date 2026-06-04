"""
Topic: Constructors in Python

A constructor is a special method that is automatically
called when an object is created.

In Python, the constructor method is __init__().
"""


# --------------------------------------------------
# Basic Constructor Example
# --------------------------------------------------

class Student:
    num = 0
    def __init__(self):
        print("Student object created")


student1 = Student()
student2 = Student()


# --------------------------------------------------
# Constructor with Parameters
# --------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp1 = Employee("Rahul", 50000)
emp2 = Employee("Priya", 60000)

print("\nEmployee Details")
print("Name:", emp1.name)
print("Salary:", emp1.salary)

print()

print("Name:", emp2.name)
print("Salary:", emp2.salary)


# --------------------------------------------------
# Understanding self
# --------------------------------------------------

class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


car1 = Car("Toyota", "White")
car2 = Car("Honda", "Black")

print("\nCar Details")
print("Car 1:", car1.brand, "-", car1.color)
print("Car 2:", car2.brand, "-", car2.color)


# --------------------------------------------------
# Constructor with Default Values
# --------------------------------------------------

class Laptop:

    def __init__(self, brand, ram=8):
        self.brand = brand
        self.ram = ram


laptop1 = Laptop("Dell")
laptop2 = Laptop("HP", 16)

print("\nLaptop Details")
print(laptop1.brand, "-", laptop1.ram, "GB RAM")
print(laptop2.brand, "-", laptop2.ram, "GB RAM")


# --------------------------------------------------
# Real-World Example
# --------------------------------------------------

class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance


account1 = BankAccount("Amit", 10000)

print("\nBank Account")
print("Holder:", account1.account_holder)
print("Balance:", account1.balance)