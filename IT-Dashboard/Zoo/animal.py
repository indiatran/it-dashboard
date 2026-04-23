from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs on four legs"

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name, "Avian")
        self.can_fly = can_fly

    def speak(self):
        return "Chirp!"

    def move(self):
        if self.can_fly:
            return "Flies through the air"
        else:
            return "Waddles on the ground"

class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, "Fish")
        self.water_type = water_type

    def speak(self):
        return "Blub!"

    def move(self):
        return "Swims in the water"