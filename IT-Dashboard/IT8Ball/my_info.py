import tkinter as tk


def displayInfo(parent):
    """Display assignment info inside the GUI window."""

    info_frame = tk.Frame(parent, bg="#3c096c", bd=3, relief="ridge")
    info_frame.pack(pady=10, padx=15, fill="x")

    tk.Label(
        info_frame,
        text="✨ Assignment Information ✨",
        font=("Comic Sans MS", 14, "bold"),
        fg="#ffd6ff",
        bg="#3c096c"
    ).pack(pady=5)

    info_lines = [
        "Name: India Tran",
        "Course: Information Technology - Python",
        "Instructor: Professor Mora",
        "Assignment: Magic 8 Ball GUI",
        "Date: 04/27/2026"
    ]

    for line in info_lines:
        tk.Label(
            info_frame,
            text=line,
            font=("Arial", 10, "bold"),
            fg="white",
            bg="#3c096c"
        ).pack()