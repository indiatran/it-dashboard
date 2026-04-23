class Habitat:
    def __init__(self, name, climate, capacity):
        self.name = name
        self.climate = climate
        self.capacity = capacity
        self.animals = []

    def add_animal(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
            return f"{animal.name} added to {self.name}"
        else:
            return f"{self.name} is full, cannot add {animal.name}"

    def roll_call(self):
        for animal in self.animals:
            print(f"  {animal.describe()}")

    def __str__(self):
        return f"[{self.climate}] {self.name} ({len(self.animals)}/{self.capacity})"