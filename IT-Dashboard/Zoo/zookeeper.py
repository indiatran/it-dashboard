class Zookeeper:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.assigned_habitats = []

    def assign(self, habitat):
        self.assigned_habitats.append(habitat)

    def daily_report(self):
        report = f"Keeper: {self.name} ({self.specialty})\n"
        for habitat in self.assigned_habitats:
            report += f"  {habitat}\n"
            for animal in habitat.animals:
                report += f"  {animal.describe()}\n"
        report += "\n"
        return report