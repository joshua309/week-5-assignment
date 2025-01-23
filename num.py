class Superhero:
    def __init__(self, name, power, hometown):
        self.name = name
        self.power = power
        self.hometown = hometown
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Power: {self.power}")
        print(f"Hometown: {self.hometown}")
    
    def use_power(self):
        print(f"{self.name} is using their power: {self.power}!")

class FlyingHero(Superhero):
    def __init__(self, name, power, hometown, flight_speed):
        super().__init__(name, power, hometown)
        self.flight_speed = flight_speed
    
    def display_info(self):
        super().display_info()
        print(f"Flight Speed: {self.flight_speed} km/h")
    
    def use_power(self):
        print(f"{self.name} is soaring through the sky at {self.flight_speed} km/h using their power: {self.power}!")

hero1 = Superhero("Thunderbolt", "Electricity Manipulation", "Electro City")
hero1.display_info()
hero1.use_power()

print("\n")

hero2 = FlyingHero("Skydancer", "Wind Control", "Aeros Village", 800)
hero2.display_info()
hero2.use_power()
