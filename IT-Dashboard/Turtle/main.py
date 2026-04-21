import math
import turtle
# =========================
# Calculation Functions
# =========================
def area_rectangle(l, w):
    return l * w

def perimeter_rectangle(l, w):
    return 2 * (l + w)

def area_circle(r):
    return math.pi * r * r

def circumference(r):
    return 2 * math.pi * r

def area_triangle(b, h):
    return 0.5 * b * h

def perimeter_triangle(a, b, c):
    return a + b + c
# =========================
# Drawing Functions
# =========================
def draw_rectangle(t, l, w):
    t.clear()
    t.penup()
    t.goto(-150, 100)
    t.setheading(0)
    t.pendown()
    t.color("blue")
    t.begin_fill()

    for _ in range(2):
        t.forward(l)
        t.right(90)
        t.forward(w)
        t.right(90)

    t.end_fill()
    t.penup()
    t.goto(-150, 120)
    t.color("black")
    t.write("Rectangle", font=("Arial", 14, "bold"))


def draw_circle(t, r):
    t.clear()
    t.penup()
    t.goto(0, -r)
    t.setheading(0)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

    t.penup()
    t.goto(-30, r + 20)
    t.color("black")
    t.write("Circle", font=("Arial", 14, "bold"))

def draw_triangle(t, side):
    t.clear()
    height = math.sqrt(3) / 2 * side
    t.penup()
    t.goto(-side / 2, -height / 2)
    t.setheading(0)
    t.color("green")
    t.pendown()
    t.begin_fill()
    for _ in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()

    t.penup()
    t.goto(0, height / 2 + 10)
    t.color("black")
    t.write("Triangle", align="center", font=("Arial", 14, "bold"))


def draw_all(t, rect_l, rect_w, circ_r, side):
    t.clear()
    # Draw rectangle on left side
    t.penup()
    t.goto(-260, 100)
    t.setheading(0)
    t.color("blue")
    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(rect_l)
        t.left(90)
        t.forward(rect_w)
        t.left(90)
    t.end_fill()
    t.penup()
    t.goto(-260 + rect_l / 2, 100 + 20)
    t.color("black")
    t.write("Rectangle", align="center", font=("Arial", 14, "bold"))

    # Draw circle in center
    t.penup()
    t.goto(0, -circ_r)
    t.setheading(0)
    t.color("red")
    t.pendown()
    t.begin_fill()
    t.circle(circ_r)
    t.end_fill()
    t.penup()
    t.goto(0, circ_r + 20)
    t.color("black")
    t.write("Circle", align="center", font=("Arial", 14, "bold"))

    # Draw triangle on right side
    height = math.sqrt(3) / 2 * side
    t.penup()
    t.goto(260 - side / 2, -height / 2)
    t.setheading(0)
    t.color("green")
    t.pendown()
    t.begin_fill()
    for _ in range(3):
        t.forward(side)
        t.left(120)
    t.end_fill()
    t.penup()
    t.goto(260, height / 2 + 20)
    t.color("black")
    t.write("Triangle", align="center", font=("Arial", 14, "bold"))


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():

    screen = turtle.Screen()
    screen.title("Geometry Calculator")

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)

    while True:
        print("\nGeometry Calculator")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Triangle")
        print("4. Draw All")
        print("5. Quit")

        choice = input("Choice: ").strip()

        if choice == "1":
            length = get_float("Enter length: ")
            width = get_float("Enter width: ")
            area = area_rectangle(length, width)
            perimeter = perimeter_rectangle(length, width)
            print(f"Area: {round(area, 2)} Perimeter: {round(perimeter, 2)}")
            draw_rectangle(t, length, width)

        elif choice == "2":
            radius = get_float("Enter radius: ")
            area = area_circle(radius)
            circ = circumference(radius)
            print(f"Area: {round(area, 2)} Circumference: {round(circ, 2)}")
            draw_circle(t, radius)

        elif choice == "3":
            side = get_float("Enter side length: ")
            height = math.sqrt(3) / 2 * side
            area = area_triangle(side, height)
            perimeter = perimeter_triangle(side, side, side)
            print(f"Area: {round(area, 2)} Perimeter: {round(perimeter, 2)}")
            draw_triangle(t, side)

        elif choice == "4":
            rect_l = get_float("Enter rectangle length: ")
            rect_w = get_float("Enter rectangle width: ")
            circ_r = get_float("Enter circle radius: ")
            side = get_float("Enter triangle side: ")

            rect_area = area_rectangle(rect_l, rect_w)
            rect_perim = perimeter_rectangle(rect_l, rect_w)
            circ_area = area_circle(circ_r)
            circ_perim = circumference(circ_r)
            tri_height = math.sqrt(3) / 2 * side
            tri_area = area_triangle(side, tri_height)
            tri_perim = perimeter_triangle(side, side, side)

            print(f"Rectangle -> Area: {round(rect_area, 2)} Perimeter: {round(rect_perim, 2)}")
            print(f"Circle -> Area: {round(circ_area, 2)} Circumference: {round(circ_perim, 2)}")
            print(f"Triangle -> Area: {round(tri_area, 2)} Perimeter: {round(tri_perim, 2)}")

            draw_all(t, rect_l, rect_w, circ_r, side)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    screen.bye()


if __name__ == "__main__":
    main()