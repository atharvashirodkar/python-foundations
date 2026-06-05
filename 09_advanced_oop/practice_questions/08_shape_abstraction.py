from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area():
        pass


class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def calculate_area(self):
        area = self.length * self.height
        return area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.1415 * self.radius * self.radius
        return f"{area:.1f}"


# Create Objects

rectangle = Rectangle(10, 5)
circle = Circle(5)

print("Shape Areas")
print("-----------")

print(f"Rectangle Area: {rectangle.calculate_area()}")
print(f"Circle Area: {circle.calculate_area()}")
