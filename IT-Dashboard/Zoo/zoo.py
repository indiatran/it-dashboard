class Zoo:
    def __init__(self, name):
        self.name = name
        self.habitats = []
        self.keepers = []

    def add_habitat(self, habitat):
        self.habitats.append(habitat)

    def hire_keeper(self, keeper):
        self.keepers.append(keeper)

    def total_animals(self):
        return sum(len(h.animals) for h in self.habitats)

    def full_report(self):
        report = f"=== {self.name} ===\n"
        report += f"Habitats: {len(self.habitats)}\n"
        report += f"Animals: {self.total_animals()}\n"
        report += f"Keepers: {len(self.keepers)}\n\n"
        for habitat in self.habitats:
            report += str(habitat) + "\n"
            for animal in habitat.animals:
                report += f"  {animal.describe()}\n"
            report += "\n"
        return report