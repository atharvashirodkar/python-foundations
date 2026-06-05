"""

Abstraction means hiding implementation details
and showing only essential functionality to the user.

Python provides abstraction using the abc module
(Abstract Base Classes).

"""

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


# Child Class 1
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")


# Child Class 2
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")


print("===== Abstraction =====")

car = Car()
bike = Bike()

car.start()
bike.start()