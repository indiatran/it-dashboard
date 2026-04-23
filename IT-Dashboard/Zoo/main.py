from animal import Bird, Rhino, Alligator, Dolphin
from habitat import Habitat
from zoo import Zoo
from zookeeper import Zookeeper
import tkinter as tk
import random

# Create animals
bird1 = Bird("Tweety", True)
bird2 = Bird("Penguin Pete", False)
alligator = Alligator("Snappy", 18)
rhino = Rhino("Rocky", 2)
dolphin = Dolphin("Flipper", "Ocean-Saltwater")

# Create habitats
savanna = Habitat("Savanna Exhibit", "tropical", 5)
aviary = Habitat("Sky Dome Aviary", "temperate", 10)
aquarium = Habitat("Deep Blue Aquarium", "aquatic", 20)

# Add animals to habitats
savanna.add_animal(rhino)
aviary.add_animal(bird1)
aviary.add_animal(bird2)
aquarium.add_animal(alligator)
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

# GUI with Canvas
root = tk.Tk()
root.title("Zoo Management System")
root.geometry("800x650")

canvas = tk.Canvas(root, width=800, height=600, bg="lightblue")
canvas.pack()

# Habitat positions
habitats_pos = {
    'savanna': {'x': 50, 'y': 50, 'w': 200, 'h': 150, 'center': (150, 125)},
    'aviary': {'x': 300, 'y': 50, 'w': 200, 'h': 150, 'center': (400, 125)},
    'aquarium': {'x': 50, 'y': 250, 'w': 450, 'h': 150, 'center': (275, 325)}
}

# Draw habitats
for name, pos in habitats_pos.items():
    canvas.create_rectangle(pos['x'], pos['y'], pos['x']+pos['w'], pos['y']+pos['h'], fill="green" if name == 'savanna' else "skyblue" if name == 'aviary' else "blue")
    canvas.create_text(pos['x']+pos['w']/2, pos['y']+10, text=name.capitalize(), font=("Arial", 12, "bold"))

# Animal positions and objects
animal_objects = {}
animal_positions = {
    'savanna': [(100, 100), (150, 150)],  # rhino
    'aviary': [(350, 100), (400, 150), (450, 100)],  # birds
    'aquarium': [(100, 300), (200, 350), (300, 300), (400, 350)]  # alligator, dolphin
}

# Draw animals
idx = 0
for habitat in [savanna, aviary, aquarium]:
    h_name = habitat.name.lower().split()[0]  # savanna, sky, deep -> savanna, sky, deep
    if 'savanna' in h_name:
        h_key = 'savanna'
    elif 'aviary' in h_name:
        h_key = 'aviary'
    elif 'aquarium' in h_name:
        h_key = 'aquarium'
    for i, animal in enumerate(habitat.animals):
        x, y = animal_positions[h_key][i]
        if isinstance(animal, Bird):
            if animal.can_fly:
                obj = canvas.create_polygon(x, y, x+10, y-10, x+20, y, fill="yellow")  # triangle
            else:
                obj = canvas.create_oval(x, y, x+20, y+20, fill="black")  # penguin
        elif isinstance(animal, Rhino):
            obj = canvas.create_rectangle(x, y, x+30, y+20, fill="gray")
            canvas.create_line(x+15, y, x+15, y-10, fill="black", width=3)  # horn
        elif isinstance(animal, Alligator):
            obj = canvas.create_rectangle(x, y, x+40, y+15, fill="green")
        elif isinstance(animal, Dolphin):
            obj = canvas.create_oval(x, y, x+25, y+15, fill="gray")
        animal_objects[animal.name] = {'obj': obj, 'x': x, 'y': y, 'habitat': h_key}

# Golf cart
cart_x, cart_y = 400, 500
cart = canvas.create_rectangle(cart_x-15, cart_y-10, cart_x+15, cart_y+10, fill="red")
canvas.create_text(cart_x, cart_y, text="Cart", font=("Arial", 8))

# Instructions
instructions = canvas.create_text(400, 580, text="Press 1: Savanna, 2: Aviary, 3: Aquarium | When at habitat, press F to feed", font=("Arial", 10))

# Animation
def animate_animals():
    for name, data in animal_objects.items():
        dx = random.randint(-5, 5)
        dy = random.randint(-5, 5)
        canvas.move(data['obj'], dx, dy)
        data['x'] += dx
        data['y'] += dy
    root.after(1000, animate_animals)

animate_animals()

# Key bindings
current_habitat = None

def move_cart(habitat_key):
    global current_habitat
    center = habitats_pos[habitat_key]['center']
    canvas.coords(cart, center[0]-15, center[1]-10, center[0]+15, center[1]+10)
    canvas.coords(canvas.create_text(center[0], center[1], text="Cart"), center[0], center[1])
    current_habitat = habitat_key

def feed_animals():
    if current_habitat:
        for animal in [savanna, aviary, aquarium]:
            h_name = animal.name.lower().split()[0]
            if current_habitat in h_name or (current_habitat == 'aviary' and 'sky' in h_name) or (current_habitat == 'aquarium' and 'deep' in h_name):
                for a in animal.animals:
                    food_text = canvas.create_text(animal_objects[a.name]['x'], animal_objects[a.name]['y']-20, text=a.favorite_food, fill="red", font=("Arial", 10))
                    canvas.after(2000, lambda t=food_text: canvas.delete(t))
                break

root.bind('1', lambda e: move_cart('savanna'))
root.bind('2', lambda e: move_cart('aviary'))
root.bind('3', lambda e: move_cart('aquarium'))
root.bind('f', lambda e: feed_animals())

root.mainloop()