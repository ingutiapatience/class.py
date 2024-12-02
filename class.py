# Superhero class
class Superhero:
    def __init__(self, name, power, strength_level):
        self.name = name
        self.power = power
        self.strength_level = strength_level

    def display_abilities(self):
        return f"{self.name} has the power of {self.power} with a strength level of {self.strength_level}."

    def use_power(self):
        return f"{self.name} is using their power of {self.power}!"

# Inheriting from Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, strength_level, flight_speed):
        super().__init__(name, power, strength_level)
        self.flight_speed = flight_speed

    def display_abilities(self):
        parent_abilities = super().display_abilities()
        return f"{parent_abilities} They can also fly at a speed of {self.flight_speed} km/h."

    def fly(self):
        return f"{self.name} is flying at {self.flight_speed} km/h!"

# Creating an instance of Superhero
spiderman = Superhero("Spiderman", "Web-Slinging", 8)
print(spiderman.display_abilities())
print(spiderman.use_power())

# Creating an instance of FlyingSuperhero
superman = FlyingSuperhero("Superman", "Super Strength", 10, 500)
print(superman.display_abilities())
print(superman.fly())
