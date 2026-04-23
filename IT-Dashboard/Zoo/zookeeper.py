class Zookeeper:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.assigned_habitats = []

    def assign(self, habitat):
        self.assigned_habitats.append(habitat)

    def daily_report(self):
        print(f"Keeper: {self.name} ({self.specialty})")
        for habitat in self.assigned_habitats:
            print(f"  {habitat}")
            habitat.roll_call()
        print()