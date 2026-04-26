from animal import Fish, Lion, Elephant, Giraffe, Eagle, Penguin, Dolphin, Alligator, Rhino, Zebra
from habitat import Habitat
from zoo import Zoo
from zookeeper import Zookeeper
import tkinter as tk
import random
import math


# -----------------------------
# Data setup
# -----------------------------
lion = Lion("Leo")
elephant = Elephant("Ellie")
giraffe = Giraffe("Sunny")
zebra = Zebra("Zara")
rhino = Rhino("Rocky", 2)

eagle = Eagle("Skye")
penguin = Penguin("Piper")

dolphin = Dolphin("Flipper", "saltwater")
alligator = Alligator("Snappy", 18)
fish = Fish("Bubbles", "Clownfish", "Krill", "saltwater")

savanna = Habitat("Savanna Exhibit", "tropical", 8)
aviary = Habitat("Sky Dome Aviary", "temperate", 6)
aquarium = Habitat("Deep Blue Aquarium", "aquatic", 8)

savanna.add_animal(lion)
savanna.add_animal(elephant)
savanna.add_animal(giraffe)
savanna.add_animal(zebra)
savanna.add_animal(rhino)

aviary.add_animal(eagle)
aviary.add_animal(penguin)

aquarium.add_animal(dolphin)
aquarium.add_animal(alligator)
aquarium.add_animal(fish)

zoo = Zoo("Hexworth Wildlife Park")
zoo.add_habitat(savanna)
zoo.add_habitat(aviary)
zoo.add_habitat(aquarium)

keeper1 = Zookeeper("Sara", "Savanna Animals")
keeper1.assign(savanna)

keeper2 = Zookeeper("Mason", "Birds and Aquatics")
keeper2.assign(aviary)
keeper2.assign(aquarium)

zoo.hire_keeper(keeper1)
zoo.hire_keeper(keeper2)

print(zoo.full_report())
print(keeper1.daily_report())
print(keeper2.daily_report())


# -----------------------------
# Prices / revenue
# -----------------------------
TICKET_PRICE = 25
BURGER_PRICE = 8
HOTDOG_PRICE = 6
PIZZA_PRICE = 7

ticket_revenue = 0
food_revenue = 0

burger_sold = 0
hotdog_sold = 0
pizza_sold = 0


# -----------------------------
# Window / canvas
# -----------------------------
root = tk.Tk()
root.title("Hexworth Wildlife Park")
root.geometry("1280x820")
root.configure(bg="#dff4ff")

canvas = tk.Canvas(root, width=1280, height=820, bg="#dff4ff", highlightthickness=0)
canvas.pack()

root.focus_force()
canvas.focus_set()


# -----------------------------
# Page layout
# -----------------------------
MAP_W = 760
SIDEBAR_X1 = 780
SIDEBAR_X2 = 1245

canvas.create_rectangle(0, 0, 1280, 820, fill="#d9f2d4", outline="")
canvas.create_rectangle(0, 620, 1280, 820, fill="#b9df9f", outline="")
canvas.create_rectangle(0, 0, MAP_W, 820, fill="#d7f4d2", outline="")

canvas.create_rectangle(0, 610, 1280, 670, fill="#d8c4a8", outline="")
canvas.create_rectangle(675, 0, 755, 820, fill="#d8c4a8", outline="")

canvas.create_rectangle(SIDEBAR_X1, 20, SIDEBAR_X2, 790, fill="#eef8ea", outline="#2d6a4f", width=2)

canvas.create_text(
    640, 26,
    text="Hexworth Wildlife Park - Interactive Zoo Experience",
    font=("Arial", 22, "bold"),
    fill="#114b2f"
)


# -----------------------------
# Decorative park items
# -----------------------------
def draw_tree(x, y, scale=1.0):
    trunk_w = 10 * scale
    trunk_h = 24 * scale
    canopy = 20 * scale
    canvas.create_rectangle(
        x - trunk_w / 2, y, x + trunk_w / 2, y + trunk_h,
        fill="#8b5a2b", outline="#6d3b16"
    )
    canvas.create_oval(
        x - canopy, y - canopy,
        x + canopy, y + canopy * 0.6,
        fill="#2e8b57", outline="#1f6f46"
    )
    canvas.create_oval(
        x - canopy * 0.7, y - canopy * 1.2,
        x + canopy * 0.7, y + canopy * 0.2,
        fill="#228b22", outline="#1c6e1c"
    )

def draw_flower(x, y, color):
    canvas.create_text(x, y, text="✿", font=("Arial", 14, "bold"), fill=color)

for x, y in [(20, 40), (110, 36), (210, 40), (320, 36), (430, 38), (545, 40), (1210, 45)]:
    draw_tree(x, y, 0.9)

for i, (x, y) in enumerate([(65, 590), (110, 590), (155, 590), (200, 590), (245, 590), (290, 590)]):
    draw_flower(x, y, ["#e63946", "#ffd60a", "#9d4edd"][i % 3])


# -----------------------------
# Habitat data
# -----------------------------
habitats_pos = {
    "savanna": {"x": 35, "y": 75, "w": 300, "h": 240, "center": (185, 195), "habitat": savanna},
    "aviary": {"x": 365, "y": 75, "w": 270, "h": 240, "center": (500, 195), "habitat": aviary},
    "aquarium": {"x": 35, "y": 365, "w": 600, "h": 220, "center": (335, 475), "habitat": aquarium}
}


# -----------------------------
# Habitat drawing
# -----------------------------
def draw_savanna_habitat(pos):
    x1, y1 = pos["x"], pos["y"]
    x2, y2 = x1 + pos["w"], y1 + pos["h"]

    canvas.create_rectangle(x1, y1, x2, y2, fill="#e7d89b", outline="#1f5b3c", width=3)

    for x in range(int(x1) + 15, int(x2) - 20, 65):
        canvas.create_arc(x, y2 - 82, x + 95, y2 - 18, start=0, extent=180,
                          style=tk.CHORD, fill="#d7c178", outline="#d7c178")

    for tx, ty in [(x1 + 40, y1 + 30), (x1 + 145, y1 + 22), (x1 + 255, y1 + 35)]:
        draw_tree(tx, ty, 0.78)

    colors = ["#e63946", "#ffd60a", "#9d4edd"]
    for i, (fx, fy) in enumerate([(x1 + 55, y2 - 33), (x1 + 95, y2 - 29), (x1 + 135, y2 - 33),
                                  (x1 + 180, y2 - 30), (x1 + 220, y2 - 34), (x1 + 265, y2 - 30)]):
        draw_flower(fx, fy, colors[i % 3])

def draw_aviary_habitat(pos):
    x1, y1 = pos["x"], pos["y"]
    x2, y2 = x1 + pos["w"], y1 + pos["h"]

    canvas.create_rectangle(x1, y1, x2, y2, fill="#d9f2c4", outline="#1f5b3c", width=3)

    for ax in range(int(x1) + 15, int(x2) - 30, 55):
        canvas.create_arc(ax, y1 + 14, ax + 42, y1 + 42, start=0, extent=180,
                          style=tk.ARC, outline="#87ceeb", width=2)

    canvas.create_line(x1 + 35, y1 + 55, x1 + 120, y1 + 30, fill="#8b5a2b", width=4)
    canvas.create_line(x1 + 150, y1 + 70, x1 + 230, y1 + 46, fill="#8b5a2b", width=4)

    for tx, ty in [(x1 + 55, y1 + 35), (x1 + 205, y1 + 30)]:
        draw_tree(tx, ty, 0.72)

    colors = ["#e63946", "#ffd60a", "#9d4edd"]
    for i, (fx, fy) in enumerate([(x1 + 45, y2 - 30), (x1 + 85, y2 - 28), (x1 + 125, y2 - 30),
                                  (x1 + 165, y2 - 28), (x1 + 205, y2 - 30), (x1 + 245, y2 - 28)]):
        draw_flower(fx, fy, colors[i % 3])

def draw_aquarium_habitat(pos):
    x1, y1 = pos["x"], pos["y"]
    x2, y2 = x1 + pos["w"], y1 + pos["h"]

    canvas.create_rectangle(x1, y1, x2, y2, fill="#bfe8ff", outline="#1f5b3c", width=3)
    canvas.create_rectangle(x1, y1, x2, y1 + 55, fill="#d8f3ff", outline="")
    canvas.create_rectangle(x1, y1 + 55, x2, y1 + 130, fill="#a9def9", outline="")
    canvas.create_rectangle(x1, y1 + 130, x2, y2, fill="#89c2d9", outline="")

    for px in range(int(x1) + 55, int(x2) - 20, 70):
        canvas.create_text(px, y2 - 45, text="🪸", font=("Arial", 15))
    for rx in range(int(x1) + 30, int(x2) - 10, 45):
        canvas.create_text(rx, y2 - 18, text="🪨", font=("Arial", 11))

    for tx, ty in [(x1 + 55, y1 + 18), (x1 + 290, y1 + 18), (x1 + 530, y1 + 18)]:
        draw_tree(tx, ty, 0.65)

    colors = ["#e63946", "#ffd60a", "#9d4edd"]
    for i, (fx, fy) in enumerate([(x1 + 95, y1 + 33), (x1 + 140, y1 + 33), (x1 + 185, y1 + 33),
                                  (x1 + 395, y1 + 33), (x1 + 440, y1 + 33), (x1 + 485, y1 + 33)]):
        draw_flower(fx, fy, colors[i % 3])

draw_savanna_habitat(habitats_pos["savanna"])
draw_aviary_habitat(habitats_pos["aviary"])
draw_aquarium_habitat(habitats_pos["aquarium"])

for key, pos in habitats_pos.items():
    canvas.create_text(
        pos["x"] + pos["w"] / 2,
        pos["y"] - 18,
        text=pos["habitat"].name,
        font=("Arial", 15, "bold"),
        fill="#114b2f"
    )
    canvas.create_text(
        pos["x"] + pos["w"] / 2,
        pos["y"] + pos["h"] + 16,
        text=f"Climate: {pos['habitat'].climate} | Capacity: {pos['habitat'].capacity}",
        font=("Arial", 10),
        fill="#1f5b3c"
    )


# -----------------------------
# Right sidebar sections
# -----------------------------
canvas.create_rectangle(800, 40, 1225, 205, fill="#f4fff1", outline="#2d6a4f", width=2)
canvas.create_text(1012, 62, text="Directions", font=("Arial", 18, "bold"), fill="#114b2f")
canvas.create_text(
    1012, 128,
    text=(
        "Keyboard: 1 = Savanna, 2 = Aviary, 3 = Aquarium, F = Feed\n"
        "Use the Go To buttons to move the cart.\n"
        "Feed Animals drops habitat food.\n"
        "Animals only eat food matching their diet.\n"
        "Buy Ticket adds one visitor.\n"
        "Food truck serves customers."
    ),
    font=("Arial", 9),
    fill="#1d3557",
    justify="center"
)

status_text = canvas.create_text(
    1012, 185,
    text="Current Stop: Entrance",
    font=("Arial", 12, "bold"),
    fill="#0b4f6c"
)

canvas.create_rectangle(800, 220, 1225, 300, fill="#effff0", outline="#2d6a4f", width=2)
canvas.create_text(1012, 242, text="Zoo Revenue", font=("Arial", 17, "bold"), fill="#114b2f")

ticket_revenue_text = canvas.create_text(840, 268, text="Ticket Revenue: $0", font=("Arial", 11, "bold"),
                                         fill="#1d3557", anchor="w")
food_revenue_text = canvas.create_text(840, 288, text="Food Truck Revenue: $0", font=("Arial", 11, "bold"),
                                       fill="#1d3557", anchor="w")
total_revenue_text = canvas.create_text(1160, 278, text="Total: $0", font=("Arial", 13, "bold"), fill="#0b4f6c")

canvas.create_rectangle(800, 320, 1225, 390, fill="#eef7ff", outline="#2d6a4f", width=2)
canvas.create_text(1012, 342, text="Zoo Controls", font=("Arial", 17, "bold"), fill="#114b2f")

canvas.create_rectangle(800, 405, 985, 555, fill="#f3ddb3", outline="#8b5e34", width=3)
canvas.create_rectangle(813, 430, 972, 532, fill="#fff7e8", outline="#8b5e34", width=2)
canvas.create_text(892, 422, text="🎟️ Ticket Booth", font=("Arial", 15, "bold"), fill="#8c4f00")
canvas.create_text(892, 462, text=f"Tickets: ${TICKET_PRICE}", font=("Arial", 12, "bold"), fill="#4a3620")

visitor_count_text = canvas.create_text(
    892, 492,
    text="Visitors: 0 / 20",
    font=("Arial", 12, "bold"),
    fill="#114b2f"
)

canvas.create_rectangle(1005, 405, 1225, 610, fill="#ffe066", outline="#d97706", width=3)
canvas.create_rectangle(1018, 430, 1212, 590, fill="#fff5bf", outline="#d97706", width=2)
canvas.create_text(1115, 422, text="🚚 Food Truck", font=("Arial", 15, "bold"), fill="#c2410c")
canvas.create_text(1115, 450, text="🍔 Burger   🌭 Hot Dog   🍕 Pizza", font=("Arial", 10, "bold"), fill="#7c2d12")
canvas.create_text(
    1115, 472,
    text=f"${BURGER_PRICE}      ${HOTDOG_PRICE}      ${PIZZA_PRICE}",
    font=("Arial", 10, "bold"),
    fill="#1d3557"
)

food_sales_text = canvas.create_text(
    1115, 582,
    text="Sold: B 0 | H 0 | P 0",
    font=("Arial", 10, "bold"),
    fill="#114b2f"
)


# -----------------------------
# Revenue / food truck displays
# -----------------------------
def update_revenue_display():
    total = ticket_revenue + food_revenue
    canvas.itemconfig(ticket_revenue_text, text=f"Ticket Revenue: ${ticket_revenue}")
    canvas.itemconfig(food_revenue_text, text=f"Food Truck Revenue: ${food_revenue}")
    canvas.itemconfig(total_revenue_text, text=f"Total: ${total}")

def update_food_sales_display():
    canvas.itemconfig(
        food_sales_text,
        text=f"Sold: B {burger_sold} | H {hotdog_sold} | P {pizza_sold}"
    )


# -----------------------------
# Zookeepers
# -----------------------------
def create_walker(x, y, emoji, label, path_points, text_color="#114b2f"):
    body = canvas.create_text(x, y, text=emoji, font=("Arial", 24))
    name = canvas.create_text(x, y - 24, text=label, font=("Arial", 10, "bold"), fill=text_color)
    return {
        "body": body,
        "name": name,
        "path": path_points,
        "path_index": 0,
        "speed": 1.5
    }

keeper_walkers = [
    create_walker(720, 350, "🧑‍🌾", "Sara", [(720, 350), (720, 250), (720, 145), (720, 250)]),
    create_walker(720, 500, "🧑‍🌾", "Mason", [(720, 500), (720, 620), (720, 740), (720, 620)])
]


# -----------------------------
# Golf cart
# -----------------------------
WALKWAY_CENTER_X = 715
cart_x, cart_y = 1110, 645
cart = canvas.create_text(cart_x, cart_y, text="🚗", font=("Arial", 28), tags="cart")
cart_route = []
cart_moving = False
cart_speed = 8
current_habitat = None


# -----------------------------
# Status / cart movement
# -----------------------------
def update_status(extra=""):
    stop_name = "Entrance" if not current_habitat else habitats_pos[current_habitat]["habitat"].name
    text = f"Current Stop: {stop_name}"
    if extra:
        text += f" | {extra}"
    canvas.itemconfig(status_text, text=text)

def build_cart_route(dest_x, dest_y):
    return [
        (WALKWAY_CENTER_X, cart_y),
        (WALKWAY_CENTER_X, dest_y),
        (dest_x, dest_y)
    ]

def animate_cart():
    global cart_x, cart_y, cart_moving

    if not cart_moving or not cart_route:
        cart_moving = False
        return

    target_x, target_y = cart_route[0]
    dx = target_x - cart_x
    dy = target_y - cart_y
    distance = math.hypot(dx, dy)

    if distance <= cart_speed:
        canvas.move("cart", dx, dy)
        cart_x = target_x
        cart_y = target_y
        cart_route.pop(0)

        if not cart_route:
            cart_moving = False
            update_status("Arrived")
            return
    else:
        move_x = (dx / distance) * cart_speed
        move_y = (dy / distance) * cart_speed
        canvas.move("cart", move_x, move_y)
        cart_x += move_x
        cart_y += move_y

    root.after(25, animate_cart)

def move_cart(habitat_key):
    global current_habitat, cart_moving, cart_route

    target_x, target_y = habitats_pos[habitat_key]["center"]
    target_y = target_y + 115

    current_habitat = habitat_key
    cart_route = build_cart_route(target_x, target_y)
    update_status("Cart driving")

    if not cart_moving:
        cart_moving = True
        animate_cart()

    root.focus_force()
    canvas.focus_set()


# -----------------------------
# Visitors
# -----------------------------
visitors = []
MAX_VISITORS = 20
person_emojis = ["🧍", "🚶", "🧑", "👩", "👨", "🧒"]
visitor_paths = [
    [(20, 640), (650, 640), (650, 785), (20, 785)],
    [(780, 640), (1240, 640), (1240, 785), (780, 785)],
    [(700, 40), (700, 300), (740, 300), (740, 40)],
    [(20, 640), (1240, 640), (1240, 665), (20, 665)]
]
next_path_index = 0

FOOD_TRUCK_SERVICE_POINT = (1115, 520)
EXIT_POINT = (1240, 785)

def create_visitor_path(start_path):
    return {
        "body": None,
        "path": start_path,
        "path_index": 1,
        "speed": random.choice([1.2, 1.4, 1.6, 1.8]),
        "state": "walking_loop",
        "carry_item": None,
        "carry_text": None,
        "return_path": None
    }

def add_visitor():
    global next_path_index, ticket_revenue

    if len(visitors) >= MAX_VISITORS:
        update_status("Zoo is full")
        return

    path = visitor_paths[next_path_index % len(visitor_paths)]
    next_path_index += 1

    x, y = path[0]
    visitor = create_visitor_path(path)
    visitor["body"] = canvas.create_text(x, y, text=random.choice(person_emojis), font=("Arial", 22))
    visitors.append(visitor)

    ticket_revenue += TICKET_PRICE
    canvas.itemconfig(visitor_count_text, text=f"Visitors: {len(visitors)} / 20")
    update_revenue_display()
    update_status("Ticket sold")

def find_available_customer():
    for visitor in visitors:
        if visitor["state"] == "walking_loop":
            return visitor
    return None

def assign_customer_to_food_truck(item_emoji):
    visitor = find_available_customer()
    if visitor is None:
        update_status("No free customer")
        return False

    bbox = canvas.bbox(visitor["body"])
    if not bbox:
        return False

    cx = (bbox[0] + bbox[2]) / 2
    cy = (bbox[1] + bbox[3]) / 2

    visitor["state"] = "going_to_truck"
    visitor["carry_item"] = item_emoji
    visitor["return_path"] = [(cx, cy), FOOD_TRUCK_SERVICE_POINT, EXIT_POINT]
    visitor["path"] = visitor["return_path"]
    visitor["path_index"] = 1
    return True


# -----------------------------
# Food truck sales
# -----------------------------
def sell_burger():
    global food_revenue, burger_sold
    if len(visitors) == 0:
        update_status("No customers yet")
        return
    if not assign_customer_to_food_truck("🍔"):
        return
    burger_sold += 1
    food_revenue += BURGER_PRICE
    update_food_sales_display()
    update_revenue_display()
    update_status("Burger sold")

def sell_hotdog():
    global food_revenue, hotdog_sold
    if len(visitors) == 0:
        update_status("No customers yet")
        return
    if not assign_customer_to_food_truck("🌭"):
        return
    hotdog_sold += 1
    food_revenue += HOTDOG_PRICE
    update_food_sales_display()
    update_revenue_display()
    update_status("Hot dog sold")

def sell_pizza():
    global food_revenue, pizza_sold
    if len(visitors) == 0:
        update_status("No customers yet")
        return
    if not assign_customer_to_food_truck("🍕"):
        return
    pizza_sold += 1
    food_revenue += PIZZA_PRICE
    update_food_sales_display()
    update_revenue_display()
    update_status("Pizza sold")


# -----------------------------
# Animal styles and diet
# -----------------------------
animal_style_map = {
    "Lion": {"emoji": "🦁", "fill": "#b8860b"},
    "Elephant": {"emoji": "🐘", "fill": "#6c757d"},
    "Giraffe": {"emoji": "🦒", "fill": "#d4a017"},
    "Zebra": {"emoji": "🦓", "fill": "#000000"},
    "Rhino": {"emoji": "🦏", "fill": "#6b7280"},
    "Eagle": {"emoji": "🦅", "fill": "#5c4033"},
    "Penguin": {"emoji": "🐧", "fill": "#111111"},
    "Dolphin": {"emoji": "🐬", "fill": "#468faf"},
    "Alligator": {"emoji": "🐊", "fill": "#2d6a4f"},
    "Fish": {"emoji": "🐠", "fill": "#ff7f11"},
    "Clownfish": {"emoji": "🐠", "fill": "#ff7f11"}
}

allowed_foods = {
    "Lion": {"🥩"},
    "Elephant": {"🍎", "🥬"},
    "Giraffe": {"🥬"},
    "Zebra": {"🥬"},
    "Rhino": {"🥬", "🍎"},
    "Eagle": {"🐟", "🐛"},
    "Penguin": {"🐟"},
    "Dolphin": {"🐟", "🦐"},
    "Alligator": {"🐟", "🥩"},
    "Fish": {"🦐"},
    "Clownfish": {"🦐"}
}

animal_states = {}
foods = []

def create_animal_sprite(animal, habitat_key, x, y):
    tag = f"animal_{animal.name.replace(' ', '_')}"
    style = animal_style_map.get(animal.species, {"emoji": "🐾", "fill": "#333333"})

    canvas.create_text(x + 1, y + 1, text=style["emoji"], font=("Arial", 30), fill="#d9d9d9", tags=tag)
    body = canvas.create_text(x, y, text=style["emoji"], font=("Arial", 30), fill=style["fill"], tags=tag)
    label = canvas.create_text(x, y - 24, text=animal.name, font=("Arial", 9, "bold"), fill="#114b2f", tags=tag)

    if animal.species == "Penguin":
        vx, vy, ground_mode = random.choice([-2, -1, 1, 2]), 0, True
    elif animal.species == "Eagle":
        vx, vy, ground_mode = random.choice([-2, -1, 1, 2]), random.choice([-2, -1, 1, 2]), False
    else:
        vx, vy, ground_mode = random.choice([-2, -1, 1, 2]), random.choice([-1, 1]), False

    animal_states[animal.name] = {
        "tag": tag,
        "body": body,
        "label": label,
        "animal": animal,
        "habitat_key": habitat_key,
        "vx": vx,
        "vy": vy,
        "ground_mode": ground_mode
    }

savanna_points = [(105, 145), (180, 225), (270, 120), (110, 210), (285, 185)]
aviary_points = [(430, 170), (505, 250)]
aquarium_points = [(145, 450), (300, 500), (500, 450)]

for animal, point in zip(savanna.animals, savanna_points):
    create_animal_sprite(animal, "savanna", point[0], point[1])

for animal, point in zip(aviary.animals, aviary_points):
    create_animal_sprite(animal, "aviary", point[0], point[1])

for animal, point in zip(aquarium.animals, aquarium_points):
    create_animal_sprite(animal, "aquarium", point[0], point[1])


# -----------------------------
# Feeding
# -----------------------------
def feed_current_habitat():
    if not current_habitat:
        update_status("Move the cart first")
        return

    pos = habitats_pos[current_habitat]
    habitat_food_choices = {
        "savanna": ["🥩", "🍎", "🥬"],
        "aviary": ["🐟", "🐛"],
        "aquarium": ["🐟", "🦐", "🥩"]
    }

    for _ in range(4):
        fx = random.randint(pos["x"] + 35, pos["x"] + pos["w"] - 35)
        fy = random.randint(pos["y"] + 45, pos["y"] + pos["h"] - 35)

        if current_habitat == "aviary" and random.random() < 0.5:
            fy = pos["y"] + pos["h"] - 28

        emoji = random.choice(habitat_food_choices[current_habitat])
        item = canvas.create_text(fx, fy, text=emoji, font=("Arial", 20), tags="food")
        foods.append({"item": item, "x": fx, "y": fy, "emoji": emoji, "habitat_key": current_habitat})

    update_status("Food dropped")


# -----------------------------
# Sidebar buttons
# -----------------------------
btn_savanna = tk.Button(root, text="Go to Savanna", width=12, command=lambda: move_cart("savanna"))
btn_aviary = tk.Button(root, text="Go to Aviary", width=12, command=lambda: move_cart("aviary"))
btn_aquarium = tk.Button(root, text="Go to Aquarium", width=12, command=lambda: move_cart("aquarium"))
btn_feed = tk.Button(root, text="Feed Animals", width=12, command=feed_current_habitat)

canvas.create_window(865, 370, window=btn_savanna)
canvas.create_window(1012, 370, window=btn_aviary)
canvas.create_window(1160, 370, window=btn_aquarium)
canvas.create_window(1012, 396, window=btn_feed)

btn_ticket = tk.Button(root, text="Buy Ticket", width=12, command=add_visitor)
canvas.create_window(892, 522, window=btn_ticket)

btn_burger = tk.Button(root, text="Sell Burger", width=11, command=sell_burger, bg="#8b4513", fg="white")
btn_hotdog = tk.Button(root, text="Sell Hot Dog", width=11, command=sell_hotdog, bg="#b22222", fg="white")
btn_pizza = tk.Button(root, text="Sell Pizza", width=11, command=sell_pizza, bg="#d97706", fg="white")

canvas.create_window(1115, 515, window=btn_burger)
canvas.create_window(1115, 548, window=btn_hotdog)
canvas.create_window(1115, 581, window=btn_pizza)


# -----------------------------
# Animation helpers
# -----------------------------
def move_along_path(entity):
    body = entity["body"]
    label = entity.get("name")

    bbox = canvas.bbox(body)
    if not bbox:
        return False

    cx = (bbox[0] + bbox[2]) / 2
    cy = (bbox[1] + bbox[3]) / 2
    target_x, target_y = entity["path"][entity["path_index"]]

    dx = target_x - cx
    dy = target_y - cy
    distance = math.hypot(dx, dy)

    arrived = False
    if distance < entity["speed"] + 1:
        move_x, move_y = dx, dy
        entity["path_index"] += 1
        if entity["path_index"] >= len(entity["path"]):
            entity["path_index"] = len(entity["path"]) - 1
            arrived = True
    else:
        move_x = (dx / distance) * entity["speed"]
        move_y = (dy / distance) * entity["speed"]

    canvas.move(body, move_x, move_y)
    if label is not None:
        canvas.move(label, move_x, move_y)
    return arrived

def move_loop_path(entity):
    body = entity["body"]
    label = entity.get("name")

    bbox = canvas.bbox(body)
    if not bbox:
        return

    cx = (bbox[0] + bbox[2]) / 2
    cy = (bbox[1] + bbox[3]) / 2
    target_x, target_y = entity["path"][entity["path_index"]]

    dx = target_x - cx
    dy = target_y - cy
    distance = math.hypot(dx, dy)

    if distance < entity["speed"] + 1:
        move_x, move_y = dx, dy
        entity["path_index"] = (entity["path_index"] + 1) % len(entity["path"])
    else:
        move_x = (dx / distance) * entity["speed"]
        move_y = (dy / distance) * entity["speed"]

    canvas.move(body, move_x, move_y)
    if label is not None:
        canvas.move(label, move_x, move_y)

def animal_position(state):
    bbox = canvas.bbox(state["body"])
    if bbox:
        return (bbox[0] + bbox[2]) / 2, (bbox[1] + bbox[3]) / 2
    return 0, 0


# -----------------------------
# Animation loop
# -----------------------------
def move_visitors():
    visitors_to_remove = []

    for visitor in visitors:
        if visitor["state"] == "walking_loop":
            move_loop_path(visitor)

        elif visitor["state"] == "going_to_truck":
            arrived = move_along_path(visitor)
            if visitor["carry_item"] and visitor["carry_text"] is None:
                bbox = canvas.bbox(visitor["body"])
                if bbox:
                    x = bbox[2] + 8
                    y = bbox[1] + 8
                    visitor["carry_text"] = canvas.create_text(
                        x, y, text=visitor["carry_item"], font=("Arial", 15)
                    )

            if visitor["carry_text"] is not None:
                bbox = canvas.bbox(visitor["body"])
                if bbox:
                    x = bbox[2] + 8
                    y = bbox[1] + 8
                    canvas.coords(visitor["carry_text"], x, y)

            if arrived:
                if visitor["path"][-1] == FOOD_TRUCK_SERVICE_POINT:
                    visitor["state"] = "leaving_with_food"
                    bbox = canvas.bbox(visitor["body"])
                    if bbox:
                        cx = (bbox[0] + bbox[2]) / 2
                        cy = (bbox[1] + bbox[3]) / 2
                        visitor["path"] = [(cx, cy), EXIT_POINT]
                        visitor["path_index"] = 1

        elif visitor["state"] == "leaving_with_food":
            arrived = move_along_path(visitor)

            if visitor["carry_text"] is not None:
                bbox = canvas.bbox(visitor["body"])
                if bbox:
                    x = bbox[2] + 8
                    y = bbox[1] + 8
                    canvas.coords(visitor["carry_text"], x, y)

            if arrived:
                visitors_to_remove.append(visitor)

    for visitor in visitors_to_remove:
        canvas.delete(visitor["body"])
        if visitor["carry_text"] is not None:
            canvas.delete(visitor["carry_text"])
        if visitor in visitors:
            visitors.remove(visitor)
        canvas.itemconfig(visitor_count_text, text=f"Visitors: {len(visitors)} / 20")

def move_keepers():
    for keeper in keeper_walkers:
        move_loop_path(keeper)

def move_animals():
    global foods
    foods_to_remove = []

    for state in animal_states.values():
        bbox = canvas.bbox(state["body"])
        if not bbox:
            continue

        habitat_box = habitats_pos[state["habitat_key"]]
        left, top, right, bottom = bbox
        dx, dy = state["vx"], state["vy"]

        min_x = habitat_box["x"] + 15
        max_x = habitat_box["x"] + habitat_box["w"] - 15
        min_y = habitat_box["y"] + 18
        max_y = habitat_box["y"] + habitat_box["h"] - 15

        animal_x, animal_y = animal_position(state)

        edible_foods = [
            f for f in foods
            if f["habitat_key"] == state["habitat_key"]
            and f["emoji"] in allowed_foods.get(state["animal"].species, set())
        ]

        if edible_foods:
            nearest = min(edible_foods, key=lambda f: ((f["x"] - animal_x) ** 2 + (f["y"] - animal_y) ** 2))

            if abs(nearest["x"] - animal_x) < 18 and abs(nearest["y"] - animal_y) < 18:
                foods_to_remove.append(nearest)
                update_status(f"{state['animal'].name} is eating")
            else:
                dx = 2 if nearest["x"] > animal_x else -2
                dy = 0 if state["ground_mode"] else (2 if nearest["y"] > animal_y else -2)
        else:
            if state["ground_mode"]:
                ground_y = habitat_box["y"] + habitat_box["h"] - 28
                if left + dx < min_x or right + dx > max_x:
                    state["vx"] *= -1
                    dx = state["vx"]

                bbox_height = bottom - top
                target_top = ground_y - bbox_height
                dy = target_top - top

                if random.random() < 0.04:
                    state["vx"] = random.choice([-2, -1, 1, 2])
                    dx = state["vx"]
            else:
                if left + dx < min_x or right + dx > max_x:
                    state["vx"] *= -1
                    dx = state["vx"]
                if top + dy < min_y or bottom + dy > max_y:
                    state["vy"] *= -1
                    dy = state["vy"]

                if random.random() < 0.03:
                    state["vx"] = random.choice([-2, -1, 1, 2])
                    dx = state["vx"]
                if random.random() < 0.03:
                    state["vy"] = random.choice([-1, 1])
                    dy = state["vy"]

        canvas.move(state["tag"], dx, dy)

    unique_remove = []
    seen = set()
    for food in foods_to_remove:
        if id(food) not in seen:
            unique_remove.append(food)
            seen.add(id(food))

    for food in unique_remove:
        if food in foods:
            canvas.delete(food["item"])
            foods.remove(food)

def animate():
    move_animals()
    move_visitors()
    move_keepers()
    root.after(90, animate)


# -----------------------------
# Keyboard controls
# -----------------------------
root.bind("<Key-1>", lambda e: move_cart("savanna"))
root.bind("<Key-2>", lambda e: move_cart("aviary"))
root.bind("<Key-3>", lambda e: move_cart("aquarium"))
root.bind("<Key-f>", lambda e: feed_current_habitat())
root.bind("<Key-F>", lambda e: feed_current_habitat())


update_revenue_display()
update_food_sales_display()
update_status()
animate()
root.mainloop()