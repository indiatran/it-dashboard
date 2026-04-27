"""
All-in-One IT Utility Tool
Author: India Tran

This program includes:
1. Network Scanner
2. Log Analyzer
3. Password Strength Checker
4. Subnet Calculator
5. Device Manager with JSON save/load
"""

# =========================
# Imports and Global Values
# =========================
import socket
import json
import os
import ipaddress
from collections import Counter

DEVICE_FILE = "devices.json"


# =========================
# Helper Functions
# =========================
def safe_input(prompt):
    """Read user input safely so the program does not crash during testing."""
    try:
        return input(prompt).strip()
    except EOFError:
        # This helps automated tests exit cleanly if no more input is available.
        return "6"


def pause():
    """Give the user a clean place to pause between menu screens."""
    print()


def is_quit_command(choice):
    """Return True when the user wants to exit a menu."""
    return choice.lower() in ["6", "q", "quit", "exit"]


# =========================
# Network Scanner
# =========================
def network_scanner():
    """Scan a host for open ports in a user-given range."""
    print("\n--- Network Scanner ---")

    host = safe_input("Enter host IP or website: ")

    if host == "":
        print("Host cannot be blank.")
        return

    try:
        start_port = int(safe_input("Enter starting port: "))
        end_port = int(safe_input("Enter ending port: "))
    except ValueError:
        print("Ports must be numbers.")
        return

    # Valid TCP ports range from 1 through 65535.
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Invalid port range. Enter ports between 1 and 65535.")
        return

    print(f"\nScanning {host} from port {start_port} to {end_port}...")
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = None

        try:
            # Create a socket for each port so each connection is separate.
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((host, port))

            if result == 0:
                print(f"Port {port} is OPEN")
                open_ports.append(port)

        except socket.gaierror:
            print("Invalid host. Check the IP address or website name.")
            return
        except TimeoutError:
            print("Connection timed out.")
            return
        except OSError:
            print("Connection error.")
            return
        finally:
            # Always close the socket to avoid leaving resources open.
            if sock is not None:
                sock.close()

    if len(open_ports) == 0:
        print("No open ports found.")
    else:
        print(f"Open ports found: {open_ports}")


# =========================
# Log Analyzer
# =========================
def log_analyzer():
    """Analyze a log file and count IP addresses and error types."""
    print("\n--- Log Analyzer ---")

    file_name = safe_input("Enter log file name, example server.log: ")

    if file_name == "":
        print("File name cannot be blank.")
        return

    if not os.path.exists(file_name):
        print("Log file not found.")
        return

    ip_counter = Counter()
    error_counter = Counter()
    suspicious_entries = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            words = line.split()

            # Look through every word to find valid IP addresses.
            for word in words:
                cleaned_word = word.strip("[],:;()")
                try:
                    ipaddress.ip_address(cleaned_word)
                    ip_counter[cleaned_word] += 1
                except ValueError:
                    pass

            upper_line = line.upper()

            # Count common log severity words.
            if "CRITICAL" in upper_line:
                error_counter["CRITICAL"] += 1
            elif "ERROR" in upper_line:
                error_counter["ERROR"] += 1
            elif "WARNING" in upper_line:
                error_counter["WARNING"] += 1
            elif "FAILED" in upper_line:
                error_counter["FAILED"] += 1

            # Save lines that may be useful for security review.
            if "FAILED" in upper_line or "DENIED" in upper_line or "UNAUTHORIZED" in upper_line:
                suspicious_entries.append(line.strip())

        report_name = "log_report.txt"

        with open(report_name, "w", encoding="utf-8") as report:
            report.write("LOG ANALYSIS REPORT\n")
            report.write("===================\n\n")
            report.write(f"Lines read: {len(lines)}\n\n")

            report.write("IP Address Counts:\n")
            if ip_counter:
                for ip, count in ip_counter.items():
                    report.write(f"{ip}: {count}\n")
            else:
                report.write("No IP addresses found.\n")

            report.write("\nError Counts:\n")
            if error_counter:
                for error, count in error_counter.items():
                    report.write(f"{error}: {count}\n")
            else:
                report.write("No errors found.\n")

            report.write("\nSuspicious Entries:\n")
            if suspicious_entries:
                for entry in suspicious_entries:
                    report.write(entry + "\n")
            else:
                report.write("No suspicious entries found.\n")

        print(f"Report saved as {report_name}")

    except UnicodeDecodeError:
        print("Could not read the file. Try a plain text log file.")
    except OSError:
        print("Error reading or writing file.")


# =========================
# Password Strength Checker
# =========================
def password_strength_checker():
    """Check password strength using length, complexity, and common-password rules."""
    print("\n--- Password Strength Checker ---")

    common_passwords = ["password", "123456", "admin", "qwerty", "letmein", "welcome"]

    password = safe_input("Enter a password to check: ")

    if password == "":
        print("Password cannot be blank.")
        return

    score = 0
    problems = []

    if len(password) >= 8:
        score += 1
    else:
        problems.append("Password should be at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        problems.append("Password should include an uppercase letter.")

    if any(char.islower() for char in password):
        score += 1
    else:
        problems.append("Password should include a lowercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        problems.append("Password should include a number.")

    if any(not char.isalnum() for char in password):
        score += 1
    else:
        problems.append("Password should include a special character.")

    if password.lower() not in common_passwords:
        score += 1
    else:
        problems.append("Password is too common.")

    if score >= 5:
        print("Password strength: Strong")
    elif score >= 3:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")

    if problems:
        print("\nWays to improve:")
        for problem in problems:
            print(f"- {problem}")


# =========================
# Subnet Calculator
# =========================
def subnet_calculator():
    """Calculate network address, broadcast address, usable range, and host count."""
    print("\n--- Subnet Calculator ---")

    cidr = safe_input("Enter CIDR notation, example 192.168.1.0/24: ")

    if cidr == "":
        print("CIDR input cannot be blank.")
        return

    try:
        network = ipaddress.ip_network(cidr, strict=False)

        print(f"\nNetwork Address: {network.network_address}")
        print(f"Broadcast Address: {network.broadcast_address}")
        print(f"Subnet Mask: {network.netmask}")
        print(f"Total Addresses: {network.num_addresses}")

        # Do not convert all hosts to a list because large networks can crash.
        if network.version == 4 and network.num_addresses > 2:
            first_host = network.network_address + 1
            last_host = network.broadcast_address - 1
            usable_count = network.num_addresses - 2
            print(f"Usable Range: {first_host} - {last_host}")
            print(f"Usable Host Count: {usable_count}")
        elif network.num_addresses == 2:
            print(f"Usable Range: {network.network_address} - {network.broadcast_address}")
            print("Usable Host Count: 2")
        else:
            print("Usable Range: None")
            print("Usable Host Count: 0")

    except ValueError:
        print("Invalid CIDR notation.")


# =========================
# Device Manager Data
# =========================
def load_devices():
    """Load device records from a JSON file."""
    if not os.path.exists(DEVICE_FILE):
        return []

    try:
        with open(DEVICE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

            # Make sure the JSON file actually contains a list.
            if isinstance(data, list):
                return data

            print("Device file format is invalid. Starting with an empty list.")
            return []

    except json.JSONDecodeError:
        print("Device file is damaged. Starting with an empty list.")
        return []
    except OSError:
        print("Could not load device file.")
        return []


def save_devices(devices):
    """Save device records to a JSON file."""
    try:
        with open(DEVICE_FILE, "w", encoding="utf-8") as file:
            json.dump(devices, file, indent=4)
        print("Devices saved successfully.")
    except OSError:
        print("Could not save devices.")


# =========================
# Device Manager Actions
# =========================
def add_device(devices):
    """Add a new device record."""
    print("\n--- Add Device ---")

    hostname = safe_input("Hostname: ")
    ip_address = safe_input("IP Address: ")
    device_type = safe_input("Device Type: ")
    location = safe_input("Location: ")

    if hostname == "" or ip_address == "" or device_type == "" or location == "":
        print("All fields are required.")
        return

    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        print("Invalid IP address.")
        return

    device = {
        "hostname": hostname,
        "ip_address": ip_address,
        "device_type": device_type,
        "location": location
    }

    devices.append(device)
    print("Device added successfully.")


def list_devices(devices):
    """List all saved devices."""
    print("\n--- Device List ---")

    if len(devices) == 0:
        print("No devices found.")
        return

    for number, device in enumerate(devices, start=1):
        print(f"\nDevice #{number}")
        print(f"Hostname: {device.get('hostname', 'Unknown')}")
        print(f"IP Address: {device.get('ip_address', 'Unknown')}")
        print(f"Type: {device.get('device_type', 'Unknown')}")
        print(f"Location: {device.get('location', 'Unknown')}")


def search_device(devices):
    """Search for a device by hostname."""
    search_name = safe_input("Enter hostname to search: ")

    if search_name == "":
        print("Search cannot be blank.")
        return

    for device in devices:
        if device.get("hostname", "").lower() == search_name.lower():
            print("\nDevice found:")
            print(f"Hostname: {device.get('hostname', 'Unknown')}")
            print(f"IP Address: {device.get('ip_address', 'Unknown')}")
            print(f"Type: {device.get('device_type', 'Unknown')}")
            print(f"Location: {device.get('location', 'Unknown')}")
            return

    print("Device not found.")


def delete_device(devices):
    """Delete a device by hostname."""
    delete_name = safe_input("Enter hostname to delete: ")

    if delete_name == "":
        print("Hostname cannot be blank.")
        return

    for device in devices:
        if device.get("hostname", "").lower() == delete_name.lower():
            devices.remove(device)
            print("Device deleted successfully.")
            return

    print("Device not found.")


# =========================
# Menus
# =========================
def device_manager():
    """Run the device manager menu."""
    devices = load_devices()

    while True:
        print("\n--- Device Manager ---")
        print("1. Add Device")
        print("2. List Devices")
        print("3. Search Device")
        print("4. Delete Device")
        print("5. Save Devices")
        print("6. Back to Main Menu")

        choice = safe_input("Choose an option: ")

        if choice == "1":
            add_device(devices)
        elif choice == "2":
            list_devices(devices)
        elif choice == "3":
            search_device(devices)
        elif choice == "4":
            delete_device(devices)
        elif choice == "5":
            save_devices(devices)
        elif is_quit_command(choice):
            save_devices(devices)
            break
        else:
            print("Invalid choice. Enter a number from 1 to 6.")


def show_main_menu():
    """Display the main program menu."""
    print("\n========== ALL-IN-ONE IT UTILITY TOOL ==========")
    print("1. Network Scanner")
    print("2. Log Analyzer")
    print("3. Password Strength Checker")
    print("4. Subnet Calculator")
    print("5. Device Manager")
    print("6. Exit")


def main():
    """Run the main program loop."""
    while True:
        show_main_menu()

        choice = safe_input("Choose an option: ")

        if choice == "1":
            network_scanner()
        elif choice == "2":
            log_analyzer()
        elif choice == "3":
            password_strength_checker()
        elif choice == "4":
            subnet_calculator()
        elif choice == "5":
            device_manager()
        elif is_quit_command(choice):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 6.")


# =========================
# Program Start
# =========================
if __name__ == "__main__":
    main()