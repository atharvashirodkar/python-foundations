"""

Polymorphism means "many forms".

The same method name can behave differently
for different objects.

"""

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


# Child Class 3
class Cow(Animal):
    def sound(self):
        print("Cow moos")


print("===== Polymorphism =====")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()