'''

Method Overriding occurs when a child class provides
its own implementation of a method that already exists
in the parent class.

'''

# Parent Class
class Animal:
    def sound(self):
        print("Animals make sounds")


# Child Class 1
class Dog(Animal):
    def sound(self):
        print("Dog barks")


# Child Class 2
class Cat(Animal):
    def sound(self):
        print("Cat meows")


print("===== Method Overriding =====")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# ==================================================
# Using super()
# ==================================================

class Employee:
    def show_role(self):
        print("Employee works in the organization")


class Manager(Employee):
    def show_role(self):
        super().show_role()   # Call parent method
        print("Manager manages the team")


print("\n===== Using super() =====")

manager = Manager()
manager.show_role()