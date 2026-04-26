"""
IT Dashboard — COP1034C Python for IT
India Tran | 4/25/26

Description: Integrated IT tool for manual disk monitoring, automated log analysis, 
and network device management.
"""

from datetime import datetime 
import sys
import os
import turtle

APP_NAME = "IT Dashboard"
VERSION = "0.3.0" 

# --- Week 3 Class Definitions ---

class NetworkDevice:
    """Base class representing a generic network device."""

    def __init__(self, hostname, ip_address, device_type, status="online"):
        """Initialize a NetworkDevice with identity and status fields."""
        self.hostname = hostname
        self.ip_address = ip_address
        self.device_type = device_type
        self.status = status

    def __str__(self):
        """Return a one-line summary string for this device."""
        return f"[{self.device_type}] {self.hostname} | {self.ip_address} | Status: {self.status}"

    def ping(self):
        """Simulate a ping to this device and return a result string."""
        return f"Reply from {self.ip_address}: bytes=32 time=2ms TTL=64"

    def get_info(self):
        """Return a formatted string with this device's details."""
        return str(self)

    def set_status(self, new_status):
        """Update the device status to the given string."""
        self.status = new_status

class Router(NetworkDevice):
    """A network router. Extends NetworkDevice with routing information."""

    def __init__(self, hostname, ip_address, routing_protocol="OSPF"):
        """Initialize a Router — calls super().__init__ with device_type='router'."""
        super().__init__(hostname, ip_address, device_type="router")
        self.routing_protocol = routing_protocol
        self.routes = ["10.0.0.0/8", "192.168.1.0/24", "0.0.0.0/0"]

    def get_info(self):
        """Override base get_info to include routing protocol and routes."""
        base_line = super().get_info()
        return f"{base_line}\n  Protocol : {self.routing_protocol}\n  Routes   : {', '.join(self.routes)}"

    def show_routes(self):
        """Return a list of routes this router knows about."""
        return self.routes

    def add_route(self, route):
        """Add a route string to this router's route list."""
        self.routes.append(route)

class Switch(NetworkDevice):
    """A network switch. Extends NetworkDevice with VLAN and port information."""

    def __init__(self, hostname, ip_address, port_count=24):
        """Initialize a Switch — calls super().__init__ with device_type='switch'."""
        super().__init__(hostname, ip_address, device_type="switch")
        self.port_count = port_count
        self.vlans = ["VLAN 1 (default)", "VLAN 10 (Sales)"]

    def get_info(self):
        """Override base get_info to include port count and VLAN list."""
        base_line = super().get_info()
        return f"{base_line}\n  Ports    : {self.port_count}\n  VLANs    : {', '.join(self.vlans)}"

    def show_vlans(self):
        """Return the current list of VLAN description strings."""
        return self.vlans

    def add_vlan(self, vlan_description):
        """Add a VLAN description string to this switch's VLAN list."""
        self.vlans.append(vlan_description)

class DeviceManager:
    """Manages a collection of NetworkDevice objects."""

    def __init__(self):
        """Initialize with an empty device list."""
        self.devices = []

    def add_device(self, device):
        """Add a NetworkDevice (or subclass) to the devices list."""
        self.devices.append(device)

    def remove_device(self, hostname):
        """Remove the device with the given hostname. Print a message if not found."""
        target = self.find_device(hostname)
        if target:
            self.devices.remove(target)
            print(f"\n[SUCCESS] Device '{hostname}' removed from inventory.")
        else:
            print(f"\n[ERROR] Device '{hostname}' not found.")

    def find_device(self, hostname):
        """Return the device object matching hostname, or None if not found."""
        for device in self.devices:
            if device.hostname.lower() == hostname.lower():
                return device
        return None

    def list_all(self):
        """Print the get_info() output for every device in the list."""
        if not self.devices:
            print("\n[!] No devices in manager.")
            return
        print("\n--- Network Device Inventory ---")
        for device in self.devices:
            # Demonstrating Polymorphism
            print(device.get_info())
            print("-" * 40)

# --- Week 3 Top-level Menu Functions ---

def draw_topology(manager):
    """Draw a simple network topology using turtle."""
    if not manager.devices:
        print("\n[!] No devices to draw.")
        return

    print("\nOpening Topology View... (Close window to return to menu)")
    screen = turtle.Screen()
    screen.title("Network Topology Visualization")
    screen.bgcolor("#0a0e1a")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    x_start = -200
    x_step  =  150
    y_pos   =    0

    for i, device in enumerate(manager.devices):
        x = x_start + (i * x_step)
        t.penup()
        t.goto(x, y_pos)
        t.pendown()

        # Color based on device type
        t.fillcolor("#10b981" if device.device_type == "router" else "#3b82f6")

        t.begin_fill()
        for _ in range(2):
            t.forward(60)
            t.left(90)
            t.forward(40)
            t.left(90)
        t.end_fill()

        t.penup()
        t.goto(x + 30, y_pos - 25)
        t.color("white")
        t.write(device.hostname, align="center", font=("Arial", 10, "bold"))

    turtle.done()

def handle_add(manager):
    """Prompt user to add a new device and add it to the manager."""
    print("\n--- Add New Device ---")
    print("1) Router")
    print("2) Switch")
    choice = input("Select type: ")
    
    name = input("Hostname   : ")
    ip   = input("IP Address : ")

    if choice == "1":
        proto = input("Routing Protocol (OSPF/BGP): ")
        manager.add_device(Router(name, ip, proto))
    elif choice == "2":
        try:
            ports = int(input("Port Count : "))
            manager.add_device(Switch(name, ip, ports))
        except ValueError:
            print("[!] Invalid input. Defaulting to 24 ports.")
            manager.add_device(Switch(name, ip, 24))
    print("\n[SUCCESS] Device added to inventory.")

# --- Main Program ---

def main():
    # --- Week 1 Variable Declarations ---
    server_name = "Not entered"
    ip_address  = "Not entered"
    department  = "Not entered"
    total_disk_gb = 0
    used_disk_gb  = 0
    usage_pct     = 0.0
    report_ready  = False

    # Paths for Week 2 Logic
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(base_dir, "server.log")
    logs_folder = os.path.join(base_dir, "Logs")
    output_path = os.path.join(logs_folder, "log_summary.txt")

    # --- Week 3 Manager Initialization ---
    manager = DeviceManager()

    # --- Main Menu Loop ---
    while True:
        print(f"\n--- {APP_NAME} v{VERSION} ---")
        print("1) Enter server info")
        print("2) View report")
        print("3) Student Info")
        print("4) File Analysis") 
        print("5) Network Device")
        print("6) Exit")

        choice = input("\nSelect an option: ")

        # --- Option 1: Manual Input ---
        if choice == "1":
            print("\n--- Enter Server Details ---")
            server_name = input("Server Name : ")
            ip_address  = input("IP Address  : ")
            department  = input("Department  : ")
            
            try:
                total_disk_gb = int(input("Total Disk (GB): "))
                used_disk_gb  = int(input("Used Disk (GB) : "))

                if total_disk_gb <= 0:
                    print("\n[!] Error: Total disk must be greater than 0.")
                    report_ready = False
                elif used_disk_gb > total_disk_gb:
                    print("\n[!] Error: Used disk cannot exceed total disk.")
                    report_ready = False
                elif used_disk_gb < 0 or total_disk_gb < 0:
                    print("\n[!] Error: Values cannot be negative.")
                    report_ready = False
                else:
                    usage_pct = (used_disk_gb / total_disk_gb) * 100
                    report_ready = True
                    print("\nData saved successfully!")
            except ValueError:
                print("\n[!] Error: Please enter valid numeric whole numbers.")

        # --- Option 2: View Manual Report ---
        elif choice == "2":
            if not report_ready:
                print("\n[!] Please enter data first (Option 1).")
            else:
                if usage_pct > 90:
                    status = "CRITICAL - Immediate action required"
                elif usage_pct > 75:
                    status = "WARNING - Disk usage is elevated"
                else:
                    status = "OK - Disk usage is normal"

                print("\n" + "="*40)
                print(f"{'IT SYSTEM STATUS REPORT':^40}")
                print("="*40)
                print(f"{'Server Name':<15}: {server_name}")
                print(f"{'IP Address':<15}: {ip_address}")
                print(f"{'Department':<15}: {department}")
                print("-" * 40)
                print(f"{'Total Disk':<15}: {total_disk_gb} GB")
                print(f"{'Used Disk':<15}: {used_disk_gb} GB")
                print(f"{'Free Disk':<15}: {total_disk_gb - used_disk_gb} GB")
                print(f"{'Usage':<15}: {usage_pct:.2f}%")
                print(f"{'Status':<15}: {status}")
                print("="*40)

                checks = ["Ping response", "DNS resolution", "Firewall active"]
                print("\nSystem Health Checks:")
                for check in checks:
                    print(f"  - {check:<18}: PASS")

        # --- Option 3: Student Info ---
        elif choice == "3":
            name = "India Tran"
            course = "Programming for IT Professionals"
            instructor = "Professor Mora"
            assignment = "Week 2 Project"
            today = datetime.now().strftime("%m/%d/%Y")

            print("\n" + "~"*50)
            print(f"{'STUDENT & COURSE INFORMATION':^50}")
            print("~"*50)
            print(f"{'Name':<15}: {name}")
            print(f"{'Course':<15}: {course}")
            print(f"{'Instructor':<15}: {instructor}")
            print(f"{'Assignment':<15}: {assignment}")
            print(f"{'Date':<15}: {today}")
            print("~"*50)

        # --- Option 4: Log File Analysis ---
        elif choice == "4":
            severity_counts = {}
            unique_errors = set()
            log_entries = []

            try:
                if not os.path.exists(log_path):
                    raise FileNotFoundError

                with open(log_path, 'r') as f:
                    for line in f:
                        clean_line = line.strip()
                        if not clean_line: continue
                        
                        date_comp = clean_line[0:10] # Using slicing
                        parts = clean_line.split(maxsplit=3)
                        
                        if len(parts) >= 4:
                            sev = parts[2].strip("[]").upper()
                            msg = parts[3]
                            severity_counts[sev] = severity_counts.get(sev, 0) + 1
                            if sev == "ERROR": unique_errors.add(msg)
                            log_entries.append({"date": date_comp, "severity": sev, "message": msg})

                total = len(log_entries)
                err_list = [e for e in log_entries if e['severity'] == "ERROR"] # List Comprehension
                err_rate = (len(err_list) / total * 100) if total > 0 else 0.0

                if not os.path.exists(logs_folder):
                    os.makedirs(logs_folder)

                with open(output_path, 'w') as out:
                    lines = [
                        "\n" + "=" * 36,
                        f"{'SERVER LOG ANALYSIS REPORT':^36}",
                        "=" * 36,
                        f"{'Log File':<12}: server.log",
                        f"{'Lines Read':<12}: {total}",
                        "-" * 36,
                        "SEVERITY COUNTS"
                    ]
                    for level in ["INFO", "WARNING", "ERROR", "CRITICAL"]:
                        count = severity_counts.get(level, 0)
                        lines.append(f"  {level:<9} : {count:>2}")
                    
                    lines.append("-" * 36)
                    lines.append(f"ERROR RATE  : {err_rate:.2f}%")
                    lines.append("-" * 36)
                    lines.append(f"UNIQUE ERRORS ({len(unique_errors)} total)")
                    for err in sorted(unique_errors):
                        lines.append(f"  - {err}")
                    
                    crits = [e['message'] for e in log_entries if e['severity'] == "CRITICAL"]
                    lines.append(f"CRITICAL EVENTS ({len(crits)} total)")
                    for msg in crits:
                        lines.append(f"  - {msg}")
                    lines.append("=" * 36)

                    for l in lines:
                        print(l)
                        print(l, file=out)

                print(f"\n[SUCCESS] Report generated in: {output_path}")

            except FileNotFoundError:
                print(f"\n[ERROR] Python cannot find 'server.log' at {log_path}")

        # --- Option 5: Network Device Lab (Week 3 Logic) ---
        elif choice == "5":
            while True:
                print("\n" + "*"*40)
                print(f"{'NETWORK DEVICE MANAGER':^40}")
                print("*"*40)
                print("A) Add Device")
                print("B) List All Devices")
                print("C) Remove Device")
                print("D) Ping Device")
                print("E) Draw Topology")
                print("F) Back to Main Menu")

                sub_choice = input("\nSelect an action: ").upper()

                if sub_choice == "A":
                    handle_add(manager) # Requirement 6
                elif sub_choice == "B":
                    manager.list_all()  # Requirement 5/9
                elif sub_choice == "C":
                    name = input("Enter hostname to remove: ")
                    manager.remove_device(name)
                elif sub_choice == "D":
                    name = input("Enter hostname to ping: ")
                    device = manager.find_device(name)
                    if device:
                        print(f"\n{device.ping()}")
                    else:
                        print("\n[!] Device not found.")
                elif sub_choice == "E":
                    draw_topology(manager) # Requirement 7
                elif sub_choice == "F":
                    break
                else:
                    print("\n[!] Invalid selection.")

        # --- Option 6: Exit ---
        elif choice == "6":
            print(f"\nExiting {APP_NAME}. Goodbye!")
            break

        else:
            print("\n[!] Invalid choice.")

if __name__ == "__main__":
    main()