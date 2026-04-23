from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, species):
        self.name = name
        self.species = species

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

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")
        self.breed = breed

    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs fast."

    def habitat(self):
        return "Dogs usually live in homes, farms, or shelters with people."

class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name, "Avian")
        self.can_fly = can_fly

    def speak(self):
        return "Chirp!"

    def move(self):
        if self.can_fly:
            return "Flies high."
        else:
            return "Waddles on the ground."

    def habitat(self):
        return "Birds live in trees, forests, nests, and open skies."

class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, "Fish")
        self.water_type = water_type

    def speak(self):
        return "Blub!"

    def move(self):
        return "Swims around."

    def habitat(self):
        return "Fish live in rivers, lakes, ponds, and oceans."

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Feline")
        self.breed = breed

    def speak(self):
        return "Meow!"

    def move(self):
        return "Sneaks quietly."

    def habitat(self):
        return "Cats usually live in homes, streets, or barns."

class Dolphin(Animal):
    def __init__(self, name, water_type):
        super().__init__(name, "Cetacean")
        self.water_type = water_type

    def speak(self):
        return "Eeeee Click!"

    def move(self):
        return "Jumps through water."

    def habitat(self):
        return "Dolphins live in oceans and warm coastal waters."