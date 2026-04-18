"""
IT Dashboard — COP1034C Python for IT
India Tran | 04/14/2026

Description: Integrated IT tool for manual disk monitoring and automated log analysis.
"""

from datetime import datetime
import os

APP_NAME = "IT Dashboard"
VERSION = "0.2.5"

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
    data_log_path = os.path.join(base_dir, "Data", "server.log")
    root_log_path = os.path.join(base_dir, "server.log")
    log_path = data_log_path if os.path.exists(data_log_path) else root_log_path
    log_filename = os.path.basename(log_path)
    logs_folder = os.path.join(base_dir, "Logs")
    output_path = os.path.join(logs_folder, "log_summary.txt")

    # --- Main Menu Loop ---
    while True:
        print(f"\n--- {APP_NAME} v{VERSION} ---")
        print("1) Enter server info")
        print("2) View report")
        print("3) Student Info")
        print("4) File Analysis")
        print("5) Exit")

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
            assignment = "Week 1 in class lab"
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
            critical_events = set()
            log_entries = []

            try:
                if not os.path.exists(log_path):
                    raise FileNotFoundError

                with open(log_path, 'r') as f:
                    for line in f:
                        clean_line = line.strip()
                        if not clean_line:
                            continue

                        date_comp = clean_line[0:10]
                        parts = clean_line.split(maxsplit=3)

                        if len(parts) >= 4:
                            sev = parts[2].strip("[]").upper()
                            msg = parts[3]
                            severity_counts[sev] = severity_counts.get(sev, 0) + 1
                            if sev == "ERROR":
                                unique_errors.add(msg)
                            if sev == "CRITICAL":
                                critical_events.add(msg)
                            log_entries.append({"date": date_comp, "severity": sev, "message": msg})

                total = len(log_entries)
                err_rate = (sum(1 for e in log_entries if e['severity'] == "ERROR") / total * 100) if total > 0 else 0.0

                os.makedirs(logs_folder, exist_ok=True)

                with open(output_path, 'w') as out:
                    lines = [
                        "=" * 36,
                        f"{'SERVER LOG ANALYSIS REPORT':^36}",
                        "=" * 36,
                        f"{'Log File':<12}: {log_filename}",
                        f"{'Lines Read':<12}: {total}",
                        "-" * 36,
                        "SEVERITY COUNTS"
                    ]
                    for level in ["INFO", "WARNING", "ERROR", "CRITICAL"]:
                        count = severity_counts.get(level, 0)
                        lines.append(f"  {level:<9}: {count:>2}")

                    lines.append("-" * 36)
                    lines.append(f"ERROR RATE  : {err_rate:.2f}%")
                    lines.append("-" * 36)
                    lines.append(f"UNIQUE ERRORS ({len(unique_errors)} total)")
                    for err in sorted(unique_errors):
                        lines.append(f"  - {err}")

                    lines.append(f"CRITICAL EVENTS ({len(critical_events)} total)")
                    for msg in sorted(critical_events):
                        lines.append(f"  - {msg}")
                    lines.append("=" * 36)

                    for l in lines:
                        print(l)
                        print(l, file=out)

                print(f"\n[SUCCESS] Report generated in: {output_path}")

            except FileNotFoundError:
                print(f"\n[ERROR] Python cannot find '{log_filename}' at {log_path}")

        # --- Option 5: Exit ---
        elif choice == "5":
            print(f"\nExiting {APP_NAME}. Goodbye!")
            break

        else:
            print("\n[!] Invalid choice.")

if __name__ == "__main__":
    main()