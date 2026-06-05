class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

class Puppy(Dog):
    def weep(self):
        print("Puppy can weep")

# Create Object

puppy1 = Puppy()


puppy1.eat()
puppy1.bark()
puppy1.weep()