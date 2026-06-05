class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


class Cow:
    def sound(self):
        print("Cow moos")


# Create Objects

dog = Dog()
cat = Cat()
cow = Cow()

animals = [dog, cat, cow]


for animal in animals:
    animal.sound()
