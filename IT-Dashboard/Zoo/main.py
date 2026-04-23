from animal import Bird, Fish, Cat, Dolphin
from habitat import Habitat
from zoo import Zoo
from zookeeper import Zookeeper
import tkinter as tk
from tkinter import scrolledtext

# Create animals
bird1 = Bird("Tweety", True)
bird2 = Bird("Penguin Pete", False)
fish = Fish("Nemo", "Saltwater")
cat = Cat("Whiskers", "Siamese")
dolphin = Dolphin("Flipper", "Ocean")

# Create habitats
savanna = Habitat("Savanna Exhibit", "tropical", 5)
aviary = Habitat("Sky Dome Aviary", "temperate", 10)
aquarium = Habitat("Deep Blue Aquarium", "aquatic", 20)

# Add animals to habitats
savanna.add_animal(cat)
aviary.add_animal(bird1)
aviary.add_animal(bird2)
aquarium.add_animal(fish)
aquarium.add_animal(dolphin)

# Create zoo
zoo = Zoo("Hexworth Wildlife Park")
zoo.add_habitat(savanna)
zoo.add_habitat(aviary)
zoo.add_habitat(aquarium)

# Create zookeeper
keeper = Zookeeper("Sara", "Birds")
keeper.assign(aviary)
zoo.hire_keeper(keeper)

# Create GUI
root = tk.Tk()
root.title("Zoo Management System")
root.geometry("600x400")

# Text area for reports
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
text_area.pack(pady=10)

# Display reports
report = zoo.full_report() + keeper.daily_report()
text_area.insert(tk.END, report)
text_area.config(state=tk.DISABLED)  # Make it read-only

# Run the GUI
root.mainloop()