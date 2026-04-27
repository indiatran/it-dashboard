"""India Tran's GUI Lab"""
import tkinter as tk
from tkinter import messagebox
import random

# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()
root.title("Creative Server Status Tool")
root.geometry("560x520")
root.resizable(False, False)
root.configure(bg="#1a1a2e")

# -----------------------------
# Functions
# -----------------------------
def check_status():
    ip_text = ip_entry.get().strip()
    selected_port = port_var.get()

    if not ip_text:
        messagebox.showerror("Error", "Please enter at least one server IP address.")
        return

    result_text.delete("1.0", tk.END)
    status_var.set("Checking servers...")

    ip_list = ip_text.split(",")

    for ip in ip_list:
        ip = ip.strip()

        if ip == "":
            continue

        is_online = random.choice([True, True, False])
        response_time = random.randint(10, 95)

        result_text.insert(tk.END, f"Server IP: {ip}\n")
        result_text.insert(tk.END, f"Port: {selected_port}\n")

        if is_online:
            result_text.insert(tk.END, "Status: ONLINE\n", "online")
            result_text.insert(tk.END, f"Response: {response_time}ms\n")
        else:
            result_text.insert(tk.END, "Status: OFFLINE\n", "offline")
            result_text.insert(tk.END, "Response: No response\n")

        result_text.insert(tk.END, "-" * 40 + "\n")

    status_var.set("Server check complete!")


def clear_results():
    ip_entry.delete(0, tk.END)
    result_text.delete("1.0", tk.END)
    status_var.set("Cleared")


def copy_results():
    results = result_text.get("1.0", tk.END).strip()

    if results == "":
        messagebox.showwarning("Nothing to Copy", "There are no results to copy.")
        return

    root.clipboard_clear()
    root.clipboard_append(results)
    status_var.set("Results copied to clipboard!")


def on_enter_key(event):
    check_status()


# -----------------------------
# Title
# -----------------------------
title_label = tk.Label(
    root,
    text="🌐 Server Status Tool 🌐",
    font=("Arial", 22, "bold"),
    fg="#ffcc00",
    bg="#1a1a2e"
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    root,
    text="Check one or multiple servers in style!",
    font=("Arial", 11, "italic"),
    fg="#a5f3fc",
    bg="#1a1a2e"
)
subtitle_label.pack()

# -----------------------------
# Input Frame
# -----------------------------
input_frame = tk.Frame(root, bg="#16213e", bd=3, relief="ridge")
input_frame.pack(pady=15, padx=20, fill="x")

ip_label = tk.Label(
    input_frame,
    text="Server IP(s):",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#16213e"
)
ip_label.grid(row=0, column=0, padx=10, pady=12)

ip_entry = tk.Entry(
    input_frame,
    width=35,
    font=("Consolas", 11),
    bg="#f8fafc",
    fg="#111827"
)
ip_entry.grid(row=0, column=1, padx=10, pady=12)
ip_entry.insert(0, "192.168.1.1, 10.0.0.5")

ip_entry.bind("<Return>", on_enter_key)

# -----------------------------
# Port Dropdown Bonus
# -----------------------------
port_frame = tk.Frame(root, bg="#1a1a2e")
port_frame.pack(pady=5)

port_label = tk.Label(
    port_frame,
    text="Select Port:",
    font=("Arial", 11, "bold"),
    fg="white",
    bg="#1a1a2e"
)
port_label.grid(row=0, column=0, padx=8)

port_var = tk.StringVar(value="80")

port_menu = tk.OptionMenu(
    port_frame,
    port_var,
    "21", "22", "25", "53", "80", "110", "143", "443", "3389"
)
port_menu.config(
    bg="#7c3aed",
    fg="white",
    font=("Arial", 10, "bold"),
    width=8,
    cursor="hand2"
)
port_menu.grid(row=0, column=1, padx=8)

# -----------------------------
# Buttons
# -----------------------------
btn_frame = tk.Frame(root, bg="#1a1a2e")
btn_frame.pack(pady=15)

check_btn = tk.Button(
    btn_frame,
    text="Check Status",
    command=check_status,
    font=("Arial", 11, "bold"),
    bg="#22c55e",
    fg="white",
    width=14,
    cursor="hand2"
)
check_btn.grid(row=0, column=0, padx=6)

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    command=clear_results,
    font=("Arial", 11, "bold"),
    bg="#ef4444",
    fg="white",
    width=10,
    cursor="hand2"
)
clear_btn.grid(row=0, column=1, padx=6)

copy_btn = tk.Button(
    btn_frame,
    text="Copy Results",
    command=copy_results,
    font=("Arial", 11, "bold"),
    bg="#3b82f6",
    fg="white",
    width=13,
    cursor="hand2"
)
copy_btn.grid(row=0, column=2, padx=6)

# -----------------------------
# Results Area
# -----------------------------
result_text = tk.Text(
    root,
    width=62,
    height=13,
    font=("Consolas", 10),
    bg="#020617",
    fg="#e5e7eb",
    relief="sunken",
    bd=3
)
result_text.pack(padx=20, pady=10)

result_text.tag_config("online", foreground="#22c55e")
result_text.tag_config("offline", foreground="#ef4444")

# -----------------------------
# Status Bar
# -----------------------------
status_var = tk.StringVar(value="Ready")

status_bar = tk.Label(
    root,
    textvariable=status_var,
    font=("Arial", 9, "bold"),
    fg="#cbd5e1",
    bg="#0f172a",
    anchor="w",
    padx=10
)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# -----------------------------
# Run Program
# -----------------------------
root.mainloop()