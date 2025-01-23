# polymorphism_challenge.py

class Animal:
    def move(self):
        pass

class Vehicle:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        print("The dog is running! 🐕")

class Bird(Animal):
    def move(self):
        print("The bird is flying! 🐦")

class Car(Vehicle):
    def move(self):
        print("The car is driving! 🚗")

class Plane(Vehicle):
    def move(self):
        print("The plane is flying! ✈️")

if __name__ == "__main__":
    dog = Dog()
    bird = Bird()
    car = Car()
    plane = Plane()

    animals = [dog, bird]
    vehicles = [car, plane]

    for animal in animals:
        animal.move()

    for vehicle in vehicles:
        vehicle.move()
