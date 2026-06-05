'''

Inheritance allows one class to inherit properties
and methods from another class.

Types Covered:
1. Single Inheritance
2. Multilevel Inheritance

'''

# ==================================================
# Single Inheritance
# ==================================================

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def show_course(self):
        print(f"Course: {self.course}")


print("===== Single Inheritance =====")

student1 = Student("Rahul", 20, "Python Programming")

student1.display_info()
student1.show_course()


# ==================================================
# Multilevel Inheritance
# ==================================================

class Animal:
    def eat(self):
        print("Animal can eat")


class Dog(Animal):
    def bark(self):
        print("Dog can bark")


class Puppy(Dog):
    def weep(self):
        print("Puppy can weep")


print("\n===== Multilevel Inheritance =====")

puppy1 = Puppy()

puppy1.eat()    # inherited from Animal
puppy1.bark()   # inherited from Dog
puppy1.weep()   # own method