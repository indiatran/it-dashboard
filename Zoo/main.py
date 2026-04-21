from abc import ABC, abstractmethod

# ---------------------------------
# Device Base Class
# ---------------------------------
class Device:
    def __init__(self, brand, model, assigned_to, purchase_date):
        self.brand = brand
        self.model = model
        self.assigned_to = assigned_to
        self.purchase_date = purchase_date

    def report(self):
        return "Override this in subclass"


# ---------------------------------
# Device Subclasses
# ---------------------------------
class Laptop(Device):
    def __init__(self, brand, model, assigned_to, purchase_date, ram):
        super().__init__(brand, model, assigned_to, purchase_date)
        self.ram = ram

    def report(self):
        return f"Laptop | {self.brand} {self.model} | Assigned To: {self.assigned_to} | Purchase Date: {self.purchase_date} | RAM: {self.ram}GB"


class Desktop(Device):
    def __init__(self, brand, model, assigned_to, purchase_date, storage):
        super().__init__(brand, model, assigned_to, purchase_date)
        self.storage = storage

    def report(self):
        return f"Desktop | {self.brand} {self.model} | Assigned To: {self.assigned_to} | Purchase Date: {self.purchase_date} | Storage: {self.storage}GB"


class Printer(Device):
    def __init__(self, brand, model, assigned_to, purchase_date, printer_type):
        super().__init__(brand, model, assigned_to, purchase_date)
        self.printer_type = printer_type

    def report(self):
        return f"Printer | {self.brand} {self.model} | Assigned To: {self.assigned_to} | Purchase Date: {self.purchase_date} | Type: {self.printer_type}"


# ---------------------------------
# Animal Base Class
# ---------------------------------
class Animal(ABC):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def describe(self):
        return f"{self.name} is a {self.breed}"

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass


# ---------------------------------
# Animal Subclasses
# ---------------------------------
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs fast."


class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def move(self):
        return "Flies high."


class Fish(Animal):
    def speak(self):
        return "Blub!"

    def move(self):
        return "Swims around."


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def move(self):
        return "Sneaks quietly."


class Dolphin(Animal):
    def speak(self):
        return "Eeeee Click!"

    def move(self):
        return "Jumps through water."


# ---------------------------------
# Zoo Class
# ---------------------------------
class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)

    def roll_call(self):
        print("\nWelcome to", self.name)
        print("-" * 30)
        for a in self.animals:
            print(a.describe())
            print(a.speak())
            print(a.move())
            print()

    def count(self):
        return len(self.animals)

    def loudest_animal(self):
        return max(self.animals, key=lambda a: len(a.speak()))


# ---------------------------------
# Main Program
# ---------------------------------

# Device Objects
device1 = Laptop("Dell", "Latitude", "India", "2024-02-10", 16)
device2 = Laptop("HP", "EliteBook", "Mark", "2023-08-14", 8)
device3 = Desktop("Lenovo", "ThinkCentre", "Sarah", "2022-05-20", 512)
device4 = Desktop("Acer", "Aspire", "James", "2023-01-11", 1000)
device5 = Printer("Canon", "PIXMA", "Office", "2021-11-30", "Inkjet")

assets = [device1, device2, device3, device4, device5]

print("DEVICE REPORT")
print("-" * 50)
for device in assets:
    print(device.report())


# Zoo Objects
zoo = Zoo("Hexworth Wildlife Park")

zoo.add_animal(Dog("Rex", "Shepherd"))
zoo.add_animal(Bird("Sunny", "Parrot"))
zoo.add_animal(Fish("Bubbles", "Goldfish"))
zoo.add_animal(Cat("Luna", "Siamese"))
zoo.add_animal(Dolphin("Splash", "Bottlenose"))

zoo.roll_call()

print("Total Animals:", zoo.count())

loud = zoo.loudest_animal()
print("Loudest Animal:", loud.name, "-", loud.speak())


# Break it on Purpose
try:
    broken = Animal("Error", "Unknown")
except TypeError as e:
    print("\nError Caught:", e)