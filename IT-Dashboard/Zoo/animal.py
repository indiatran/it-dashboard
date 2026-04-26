from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, species, favorite_food):
        self.name = name
        self.species = species
        self.favorite_food = favorite_food

    def describe(self):
        return f"{self.name} is a {self.species}"

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def habitat(self):
        pass


# Kept for assignment safety, but not used in main.py
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine", "Dog Food")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs fast."

    def habitat(self):
        return "Dogs usually live in homes, farms, or shelters with people."


class Bird(Animal):
    def __init__(self, name, species="Bird", favorite_food="Seeds", can_fly=True):
        super().__init__(name, species, favorite_food)
        self.can_fly = can_fly

    def speak(self):
        return "Chirp!"

    def move(self):
        return "Flies through the air." if self.can_fly else "Walks on the ground."

    def habitat(self):
        return "Birds live in nests, trees, cliffs, and aviaries."


class Fish(Animal):
    def __init__(self, name, species="Fish", favorite_food="Fish Pellets", water_type="freshwater"):
        super().__init__(name, species, favorite_food)
        self.water_type = water_type

    def speak(self):
        return "Blub!"

    def move(self):
        return "Swims through the water."

    def habitat(self):
        return f"{self.species} live in {self.water_type} water environments."


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name, "Lion", "Meat")

    def speak(self):
        return "Roar!"

    def move(self):
        return "Stalks and runs across the savanna."

    def habitat(self):
        return "Lions live in grasslands and open savannas."


class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name, "Elephant", "Fruit and Grass")

    def speak(self):
        return "Trumpet!"

    def move(self):
        return "Walks heavily and steadily."

    def habitat(self):
        return "Elephants live in grasslands, forests, and savannas."


class Giraffe(Animal):
    def __init__(self, name):
        super().__init__(name, "Giraffe", "Leaves")

    def speak(self):
        return "Hum!"

    def move(self):
        return "Walks gracefully with long strides."

    def habitat(self):
        return "Giraffes live in open woodlands and savannas."


class Rhino(Animal):
    def __init__(self, name, horn_length):
        super().__init__(name, "Rhino", "Hay")
        self.horn_length = horn_length

    def speak(self):
        return "Grunt!"

    def move(self):
        return "Charges forward with power."

    def habitat(self):
        return "Rhinos live in grasslands and savannas."


class Zebra(Animal):
    def __init__(self, name):
        super().__init__(name, "Zebra", "Grass")

    def speak(self):
        return "Bark!"

    def move(self):
        return "Trots quickly in herds."

    def habitat(self):
        return "Zebras live in grasslands and savannas."


class Penguin(Bird):
    def __init__(self, name):
        super().__init__(name, species="Penguin", favorite_food="Fish", can_fly=False)

    def speak(self):
        return "Honk!"

    def move(self):
        return "Walks on the ground and waddles near the habitat floor."

    def habitat(self):
        return "Penguins live in cold coastal areas and rocky habitats."


class Eagle(Bird):
    def __init__(self, name):
        super().__init__(name, species="Eagle", favorite_food="Small Animals", can_fly=True)

    def speak(self):
        return "Screech!"

    def move(self):
        return "Soars high and dives swiftly."

    def habitat(self):
        return "Eagles live in mountains, forests, cliffs, and aviaries."


class Alligator(Animal):
    def __init__(self, name, length):
        super().__init__(name, "Alligator", "Meat")
        self.length = length

    def speak(self):
        return "Hiss!"

    def move(self):
        return "Crawls on land and glides through water."

    def habitat(self):
        return "Alligators live in freshwater swamps, marshes, and rivers."


class Dolphin(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, "Dolphin", "Fish")
        self.water_type = water_type

    def speak(self):
        return "Click-click!"

    def move(self):
        return "Swims quickly and leaps through the water."

    def habitat(self):
        return "Dolphins live in oceans and warm coastal waters."