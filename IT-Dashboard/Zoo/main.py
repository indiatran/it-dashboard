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

    @abstractmethod
    def habitat(self):
        pass


# ---------------------------------
# Animal Subclasses
# ---------------------------------
class Dog(Animal):
    def speak(self):
        return "Woof!"

    def move(self):
        return "Runs fast."

    def habitat(self):
        return "Dogs usually live in homes, farms, or shelters with people."


class Bird(Animal):
    def speak(self):
        return "Chirp!"

    def move(self):
        return "Flies high."

    def habitat(self):
        return "Birds live in trees, forests, nests, and open skies."


class Fish(Animal):
    def speak(self):
        return "Blub!"

    def move(self):
        return "Swims around."

    def habitat(self):
        return "Fish live in rivers, lakes, ponds, and oceans."


class Cat(Animal):
    def speak(self):
        return "Meow!"

    def move(self):
        return "Sneaks quietly."

    def habitat(self):
        return "Cats usually live in homes, streets, or barns."


class Dolphin(Animal):
    def speak(self):
        return "Eeeee Click!"

    def move(self):
        return "Jumps through water."

    def habitat(self):
        return "Dolphins live in oceans and warm coastal waters."


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
            print("Habitat:", a.habitat())
            print()

    def count(self):
        return len(self.animals)

    def loudest_animal(self):
        return max(self.animals, key=lambda a: len(a.speak()))

    def show_animal_menu(self):
        while True:
            print("\nANIMAL MENU")
            print("-" * 30)
            for i in range(len(self.animals)):
                print(f"{i + 1}. See {self.animals[i].name}")
            print("6. Exit animal menu")

            choice = input("Choose an animal (1-6): ")

            if choice in ["1", "2", "3", "4", "5"]:
                animal = self.animals[int(choice) - 1]
                print("\n" + animal.describe())
                print("Sound:", animal.speak())
                print("Movement:", animal.move())
                print("Habitat:", animal.habitat())

            elif choice == "6":
                print("Exiting animal menu.")
                break

            else:
                print("Invalid choice.")


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

zoo.add_animal(Dog("Rex", "German Shepherd"))
zoo.add_animal(Bird("Sunny", "Parrot"))
zoo.add_animal(Fish("Bubbles", "Goldfish"))
zoo.add_animal(Cat("Luna", "Siamese"))
zoo.add_animal(Dolphin("Splash", "Bottlenose"))

zoo.roll_call()

print("Total Animals:", zoo.count())

loud = zoo.loudest_animal()
print("Loudest Animal:", loud.name, "-", loud.speak())

# Animal Menu
zoo.show_animal_menu()

# Break it on Purpose
try:
    broken = Animal("Error", "Unknown")
except TypeError as e:
    print("\nError Caught:", e)