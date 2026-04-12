"""
IT Dashboard — COP1034C Python for IT
Your Name | Date

A command-line IT management tool that grows into a full
desktop application over 4 weeks. Each class session adds
a new feature to this project.
"""

# ── Application Metadata ──────────────────────────────────
APP_NAME = "IT Dashboard"
VERSION = "0.1.0"

from datetime import datetime


def main():
    server_name = "Not entered"
    ip_address = "Not entered"
    department = "Not entered"
    total_disk_gb = 0
    used_disk_gb = 0
    usage_pct = 0.0
    report_ready = False

    while True:
        print(f"\n{APP_NAME} (v{VERSION})")
        print("1) Enter server info")
        print("2) Show report")
        print("3) Show student & course info")
        print("4) Exit")
        selection = input("Select an option: ").strip()

        if selection == "1":
            # Prompt the user to enter the server info
            server_name = input("Enter the server name: ").strip()
            ip_address = input("Enter the IP address: ").strip()
            department = input("Enter the department: ").strip()
            try:
                total_disk_gb = int(input("Enter the total disk (GB): ").strip())
                used_disk_gb = int(input("Enter the used disk (GB): ").strip())
            except ValueError:
                print("Disk values must be integers. Entry canceled.")
                continue
            if total_disk_gb > 0:
                usage_pct = (used_disk_gb / total_disk_gb) * 100
            else:
                usage_pct = 0.0
            report_ready = True

        elif selection == "2":
            if not report_ready:
                print("No report data entered yet. Please select option 1 first.")
                continue
            # Classify disk usage after calculating usage_pct
            if usage_pct > 90:
                disk_status = "CRITICAL - Immediate action required"
                status = "CRITICAL"
            elif usage_pct > 75:
                disk_status = "WARNING - Disk usage is elevated"
                status = "WARNING"
            else:
                disk_status = "OK - Disk usage is normal"
                status = "OK"

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
            checks = ["Ping response", "DNS resolution", "Firewall rule active"]
            print("System Checks:")
            for check in checks:
                print(f"  - {check}: PASS")

        elif selection == "3":
            # Data for Lab #1
            name = "India Tran"
            course = "Programming for IT Professionals"
            instructor = "Professor Mora"
            assignment = "Week 1 lab"
            # Requirement: Use datetime for current date
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

        elif selection == "4":
            print("Exiting IT Dashboard.")
            break

        else:
            print("Invalid selection. Please choose 1, 2, 3, or 4.")

# ── Run the program ───────────────────────────────────────
if __name__ == "__main__":
    main()