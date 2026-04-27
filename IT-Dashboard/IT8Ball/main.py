from my_info import displayInfo
import random
from pathlib import Path
import tkinter as tk
from tkinter import messagebox

# Show assignment info first
displayInfo()

# Read responses from text file
RESPONSES_FILE = Path(__file__).parent / "responses.txt"

try:
    with open(RESPONSES_FILE, "r", encoding="utf-8") as file:
        answers = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    messagebox.showerror("Missing File", "responses.txt was not found.")
    raise SystemExit(1)

if not answers:
    messagebox.showerror("Empty File", "No responses available in responses.txt.")
    raise SystemExit(1)


def ask_magic_ball():
    """Display a random Magic 8 Ball answer."""
    question = question_entry.get().strip()

    if question == "":
        question_label.config(text="You asked a mystery question...")
    else:
        question_label.config(text=f"You asked: {question}")

    answer = random.choice(answers)
    answer_label.config(text=answer)

    question_entry.delete(0, tk.END)


def clear_screen():
    """Clear the question and answer labels."""
    question_entry.delete(0, tk.END)
    question_label.config(text="")
    answer_label.config(text="✨ Ask me anything ✨")


def quit_app():
    """Close the program."""
    root.destroy()


# Main window
root = tk.Tk()
root.title("Whimsical Magic 8 Ball")
root.geometry("600x500")
root.resizable(False, False)
root.configure(bg="#2b1055")

# Title
title_label = tk.Label(
    root,
    text="🔮 Magic 8 Ball 🔮",
    font=("Comic Sans MS", 28, "bold"),
    fg="#ffd6ff",
    bg="#2b1055"
)
title_label.pack(pady=20)

# Magic ball display
ball_frame = tk.Frame(root, bg="#12002f", width=250, height=250)
ball_frame.pack(pady=10)
ball_frame.pack_propagate(False)

ball_label = tk.Label(
    ball_frame,
    text="8",
    font=("Arial", 80, "bold"),
    fg="white",
    bg="#12002f"
)
ball_label.pack(expand=True)

answer_label = tk.Label(
    root,
    text="✨ Ask me anything ✨",
    font=("Comic Sans MS", 16, "bold"),
    fg="#ffffff",
    bg="#2b1055",
    wraplength=500
)
answer_label.pack(pady=15)

# Question entry
question_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=40,
    justify="center",
    bg="#f8e7ff",
    fg="#2b1055"
)
question_entry.pack(pady=10)

question_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    fg="#e0aaff",
    bg="#2b1055",
    wraplength=500
)
question_label.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#2b1055")
button_frame.pack(pady=20)

ask_button = tk.Button(
    button_frame,
    text="Ask the Stars ✨",
    font=("Arial", 12, "bold"),
    bg="#ff8fab",
    fg="white",
    width=15,
    command=ask_magic_ball
)
ask_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear 🌙",
    font=("Arial", 12, "bold"),
    bg="#9d4edd",
    fg="white",
    width=12,
    command=clear_screen
)
clear_button.grid(row=0, column=1, padx=10)

quit_button = tk.Button(
    button_frame,
    text="Quit 🚪",
    font=("Arial", 12, "bold"),
    bg="#5a189a",
    fg="white",
    width=10,
    command=quit_app
)
quit_button.grid(row=0, column=2, padx=10)

# Press Enter to ask
root.bind("<Return>", lambda event: ask_magic_ball())

root.mainloop()