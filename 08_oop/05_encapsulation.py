"""
Topic: Encapsulation in Python

Encapsulation means bundling data and methods together
inside a class and controlling access to the data.

Python provides:
1. Public Members
2. Protected Members (_variable)
3. Private Members (__variable)
"""


# --------------------------------------------------
# Public Members
# --------------------------------------------------

class Student:

    def __init__(self, name):
        self.name = name      # Public Variable


student1 = Student("Rahul")

print("Public Variable:", student1.name)


# --------------------------------------------------
# Protected Members
# --------------------------------------------------

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary     # Protected Variable


emp1 = Employee("Priya", 60000)

print("\nProtected Variable:", emp1._salary)


# --------------------------------------------------
# Private Members
# --------------------------------------------------

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance      # Private Variable


account1 = BankAccount("Amit", 10000)

# print(account1.__balance)   # Error

print("\nPrivate Variable cannot be accessed directly")


# --------------------------------------------------
# Accessing Private Variables Using Methods
# --------------------------------------------------

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def get_balance(self):
        return self.__balance


account2 = BankAccount("Rahul", 15000)

print("\nCurrent Balance:", account2.get_balance())


# --------------------------------------------------
# Modifying Private Data Safely
# --------------------------------------------------

class BankAccount:

    def __init__(self, holder, balance):
        self.holder = holder
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance


account3 = BankAccount("Priya", 20000)

account3.deposit(5000)
account3.withdraw(3000)

print("\nUpdated Balance:", account3.get_balance())


# --------------------------------------------------
# Name Mangling Demonstration
# --------------------------------------------------

class Demo:

    def __init__(self):
        self.__secret = "Python"


obj = Demo()

print("\nUsing Name Mangling:")
print(obj._Demo__secret)