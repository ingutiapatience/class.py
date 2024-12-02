# Base class
class Entity:
    def move(self):
        raise NotImplementedError("Subclasses should implement this method!")

# Animal class
class Animal(Entity):
    def move(self):
        return "Walking 🐾"

# Bird class
class Bird(Entity):
    def move(self):
        return "Flying ✈️"

# Fish class
class Fish(Entity):
    def move(self):
        return "Swimming 🐟"

# Car class
class Car(Entity):
    def move(self):
        return "Driving 🚗"

# Plane class
class Plane(Entity):
    def move(self):
        return "Flying ✈️"

# Boat class
class Boat(Entity):
    def move(self):
        return "Sailing ⛵"

# Creating instances
dog = Animal()
eagle = Bird()
salmon = Fish()
sedan = Car()
jet = Plane()
yacht = Boat()

# Displaying their move actions
entities = [dog, eagle, salmon, sedan, jet, yacht]
for entity in entities:
    print(f"{type(entity).__name__} is {entity.move()}")
