class Car:
    def move(self):
        print("Car is moving")


class Plane:
    def move(self):
        print("Plane is flying")


class Boat:
    def move(self):
        print("Boat is sailing")


vehicles = [Car(), Plane(), Boat()]

for vehicle in vehicles:
    vehicle.move()
