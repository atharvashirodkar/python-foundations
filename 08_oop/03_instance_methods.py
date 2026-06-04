"""
Topic: Instance Methods in Python

Instance methods are functions defined inside a class.
They operate on object data using the self parameter.
"""


# --------------------------------------------------
# Basic Instance Method
# --------------------------------------------------

class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello,", self.name)


student1 = Student("Rahul")
student1.greet()


# --------------------------------------------------
# Multiple Instance Methods
# --------------------------------------------------

class Calculator:

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()

print("\nAddition:", calc.add(10, 20))
print("Multiplication:", calc.multiply(10, 20))


# --------------------------------------------------
# Methods Accessing Object Attributes
# --------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_details(self):
        print("\nEmployee Details")
        print("Name:", self.name)
        print("Salary:", self.salary)


emp1 = Employee("Priya", 60000)
emp1.display_details()


# --------------------------------------------------
# Updating Object Data Using Methods
# --------------------------------------------------

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.balance)


account = BankAccount("Amit", 10000)

account.deposit(2000)
account.withdraw(3000)
account.show_balance()


# --------------------------------------------------
# Real-World Example
# --------------------------------------------------

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} started.")

    def stop(self):
        print(f"{self.brand} {self.model} stopped.")


car1 = Car("Toyota", "Camry")

car1.start()
car1.stop()