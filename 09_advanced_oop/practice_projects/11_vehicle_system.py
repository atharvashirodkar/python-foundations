from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")


class Bike(Vehicle):
    def start(self):
        print("Bike started")

    def stop(self):
        print("Bike stopped")


class Truck(Vehicle):
    def start(self):
        print("Truck started")

    def stop(self):
        print("Truck stopped")


vehicles = [Car(), Bike(), Truck()]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
    print()

