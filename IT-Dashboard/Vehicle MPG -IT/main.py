"""
MPG Calculator
"""

import tkinter as tk
from tkinter import messagebox


def calculate_mpg():
    """Calculate MPG."""
    try:
        gallons = float(gallons_entry.get())
        miles = float(miles_entry.get())

        if gallons <= 0 or miles < 0:
            messagebox.showerror("Error", "Enter valid positive numbers.")
            return

        mpg = miles / gallons
        result_label.config(text=f"This vehicle gets {mpg:.2f} MPG")

    except ValueError:
        messagebox.showerror("Error", "Numbers only.")


def animate_car():
    """Move the car smoothly."""
    parts = [body, top, hood, wheel1, wheel2, rim1, rim2,
             window1, window2, headlight]

    for part in parts:
        canvas.move(part, 3, 0)

    if canvas.coords(body)[0] > 440:
        for part in parts:
            canvas.move(part, -520, 0)

    root.after(30, animate_car)


# Main Window
root = tk.Tk()
root.title("MPG Calculator")
root.geometry("440x500")
root.config(bg="#d9edf7")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="🚗 MPG Calculator 🚗",
    font=("Arial", 22, "bold"),
    bg="#d9edf7",
    fg="#003366"
)
title_label.pack(pady=15)

# Input Frame
frame = tk.Frame(root, bg="#88d0dc", padx=20, pady=20)
frame.pack()

tk.Label(
    frame,
    text="Gallons of Gas:",
    font=("Arial", 14, "bold"),
    bg="#88d0dc",
    fg="#002244"
).grid(row=0, column=0, pady=10, sticky="w")

gallons_entry = tk.Entry(frame, font=("Arial", 12), width=18)
gallons_entry.grid(row=0, column=1)

tk.Label(
    frame,
    text="Miles on Full Tank:",
    font=("Arial", 14, "bold"),
    bg="#88d0dc",
    fg="#002244"
).grid(row=1, column=0, pady=10, sticky="w")

miles_entry = tk.Entry(frame, font=("Arial", 12), width=18)
miles_entry.grid(row=1, column=1)

# Button
calc_button = tk.Button(
    root,
    text="Calculate MPG",
    font=("Arial", 13, "bold"),
    bg="#ffcc00",
    fg="black",
    command=calculate_mpg
)
calc_button.pack(pady=18)

# Result
result_label = tk.Label(
    root,
    text="Your MPG will appear here",
    font=("Arial", 16, "bold"),
    bg="#d9edf7",
    fg="#0077b6"
)
result_label.pack()

# Canvas
canvas = tk.Canvas(root, width=420, height=140, bg="#c8e7ec", highlightthickness=0)
canvas.pack(pady=18)

# Road
canvas.create_rectangle(0, 112, 420, 140, fill="#5e5e5e", outline="")
canvas.create_line(0, 126, 420, 126, fill="white", width=2, dash=(10, 8))

# Car
body = canvas.create_rectangle(40, 70, 180, 100, fill="#2b2b2b", outline="black", width=2)

top = canvas.create_polygon(
    70, 70,
    100, 45,
    145, 45,
    170, 70,
    fill="#444444",
    outline="black"
)

hood = canvas.create_polygon(
    180, 70,
    205, 78,
    205, 100,
    180, 100,
    fill="#2b2b2b",
    outline="black"
)

window1 = canvas.create_rectangle(95, 48, 118, 68, fill="#9ca3af", outline="black")
window2 = canvas.create_rectangle(123, 48, 146, 68, fill="#9ca3af", outline="black")

wheel1 = canvas.create_oval(65, 88, 100, 123, fill="black")
wheel2 = canvas.create_oval(145, 88, 180, 123, fill="black")

rim1 = canvas.create_oval(75, 98, 90, 113, fill="gray")
rim2 = canvas.create_oval(155, 98, 170, 113, fill="gray")

headlight = canvas.create_rectangle(198, 82, 205, 92, fill="yellow", outline="black")

# Animate
animate_car()

root.mainloop()