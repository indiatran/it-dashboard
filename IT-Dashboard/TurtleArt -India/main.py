# Week 3 Turtle Art Project
# Scene: A colorful house scene with grass, a sun, windows, a door, and stars in the sky
# Author: India Tran

import turtle
import random
import time

# Setup screen and turtle
screen = turtle.Screen()
screen.title("My Turtle Art")
screen.bgcolor("skyblue")

t = turtle.Turtle()
t.speed(10)          # fast drawing
t.hideturtle()       # hide the cursor arrow when done

def draw_filled_rectangle(t, x, y, width, height, fill_color):
    """Draw a filled rectangle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()

    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

    t.end_fill()


def draw_filled_triangle(t, x, y, size, fill_color):
    """Draw a filled equilateral triangle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()

    for _ in range(3):
        t.forward(size)
        t.left(120)

    t.end_fill()


def draw_filled_circle(t, x, y, radius, fill_color):
    """Draw a filled circle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_star(t, x, y, size, color):
    """Draw a single star."""
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.fillcolor(color)
    t.begin_fill()

    for _ in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()

# Grass
draw_filled_rectangle(t, -400, -200, 800, 150, "green")

# House body
draw_filled_rectangle(t, -60, -100, 120, 100, "tan")

# Door
draw_filled_rectangle(t, -15, -100, 30, 50, "brown")

# Left window
draw_filled_rectangle(t, -50, -20, 25, 25, "lightblue")

# Right window
draw_filled_rectangle(t, 25, -20, 25, 25, "lightblue")

# Roof
draw_filled_triangle(t, -60, 0, 120, "red")

# Sun
draw_filled_circle(t, 150, 100, 40, "yellow")

# Stars across the sky - randomly positioned and twinkling
screen.tracer(0)  # Turn off animation for smoother twinkling

star_turtle = turtle.Turtle()
star_turtle.speed(0)
star_turtle.hideturtle()

# Generate random positions for stars without overlaps
star_positions = []
min_distance = 50  # Minimum distance between stars to avoid overlap
while len(star_positions) < 10:
    x = random.randint(-350, 350)
    y = random.randint(100, 180)
    if all(((x - sx)**2 + (y - sy)**2)**0.5 > min_distance for sx, sy in star_positions):
        star_positions.append((x, y))

counter = 0
try:
    while True:
        color = "yellow" if counter % 2 == 0 else "white"
        star_turtle.clear()
        for x, y in star_positions:
            draw_star(star_turtle, x, y, 20, color)
        screen.update()
        time.sleep(0.5)
        counter += 1
except:
    pass

try:
    turtle.done()
except:
    pass