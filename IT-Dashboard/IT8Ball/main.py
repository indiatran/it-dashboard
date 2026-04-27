from my_info import displayInfo
import tkinter as tk
from tkinter import messagebox
import random
from pathlib import Path

# Load responses file
RESPONSES_FILE = Path(__file__).parent / "responses.txt"

try:
    with open(RESPONSES_FILE, "r", encoding="utf-8") as file:
        answers = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    answers = []

# Create main window
root = tk.Tk()
root.title("🔮 Whimsical Magic 8 Ball")
root.geometry("600x650")
root.resizable(False, False)
root.configure(bg="#2b1055")

# Show assignment info
displayInfo(root)

# Stop if no responses file
if not answers:
    messagebox.showerror("Error", "responses.txt is missing or empty.")
    root.destroy()
    raise SystemExit


def ask_magic_ball():
    """Generate random answer."""
    question = question_entry.get().strip()

    if question == "":
        question_label.config(text="You asked a mystery question...")
    else:
        question_label.config(text=f"You asked: {question}")

    answer = random.choice(answers)
    answer_label.config(text=answer)

    question_entry.delete(0, tk.END)


def clear_screen():
    """Clear question + answer."""
    question_entry.delete(0, tk.END)
    question_label.config(text="")
    answer_label.config(text="✨ Ask me anything ✨")


def quit_app():
    root.destroy()


# Title
title_label = tk.Label(
    root,
    text="🔮 Magic 8 Ball 🔮",
    font=("Comic Sans MS", 28, "bold"),
    fg="#ffd6ff",
    bg="#2b1055"
)
title_label.pack(pady=15)

# Magic ball canvas
canvas = tk.Canvas(root, width=200, height=200, bg="#2b1055", highlightthickness=0)
canvas.pack()

# Ball
canvas.create_oval(20, 20, 180, 180, fill="black", outline="#ffb3ff", width=4)

# White center
canvas.create_oval(65, 55, 135, 125, fill="white", outline="white")

# Number 8
canvas.create_text(100, 90, text="8", font=("Arial", 38, "bold"), fill="black")

# Answer label
answer_label = tk.Label(
    root,
    text="✨ Ask me anything ✨",
    font=("Comic Sans MS", 16, "bold"),
    fg="white",
    bg="#2b1055",
    wraplength=500
)
answer_label.pack(pady=15)

# Entry box
question_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=38,
    justify="center",
    bg="#f8e7ff",
    fg="#2b1055"
)
question_entry.pack(pady=10)

# Question display
question_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    fg="#e0aaff",
    bg="#2b1055",
    wraplength=500
)
question_label.pack()

# Buttons
button_frame = tk.Frame(root, bg="#2b1055")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Ask ✨",
    font=("Arial", 12, "bold"),
    bg="#ff8fab",
    fg="white",
    width=12,
    command=ask_magic_ball
).grid(row=0, column=0, padx=8)

tk.Button(
    button_frame,
    text="Clear 🌙",
    font=("Arial", 12, "bold"),
    bg="#9d4edd",
    fg="white",
    width=12,
    command=clear_screen
).grid(row=0, column=1, padx=8)

tk.Button(
    button_frame,
    text="Quit 🚪",
    font=("Arial", 12, "bold"),
    bg="#5a189a",
    fg="white",
    width=12,
    command=quit_app
).grid(row=0, column=2, padx=8)

# Press Enter key
root.bind("<Return>", lambda event: ask_magic_ball())

# Run GUI
root.mainloop()