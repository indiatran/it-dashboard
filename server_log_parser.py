import sys


def parse_log_file(log_path):
    severity_counts = {}
    unique_errors = set()
    critical_events = set()
    log_entries = []

    try:
        with open(log_path, "r") as f:
            for line in f:
                stripped_line = line.strip()
                if not stripped_line:
                    continue

                # Use slicing for the date and split the rest with maxsplit=3
                date_field = stripped_line[:10]
                parts = stripped_line.split(maxsplit=3)
                if len(parts) < 4:
                    continue

                severity = parts[2].strip("[]").upper()
                message = parts[3]

                severity_counts[severity] = severity_counts.get(severity, 0) + 1

                if severity == "ERROR":
                    unique_errors.add(message)

                if severity == "CRITICAL":
                    critical_events.add(message)

                log_entries.append({
                    "date": date_field,
                    "time": parts[1],
                    "severity": severity,
                    "message": message,
                })

    except FileNotFoundError:
        print("Error: server.log not found. Place the log file in the same directory as this script.")
        sys.exit(1)

    return severity_counts, unique_errors, critical_events, log_entries


def build_report(severity_counts, unique_errors, critical_events, log_entries):
    total_lines = len(log_entries)
    error_entries = [entry for entry in log_entries if entry["severity"] == "ERROR"]
    error_count = len(error_entries)
    error_rate = (error_count / total_lines * 100) if total_lines else 0.0

    all_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
    lines = []
    lines.append("=" * 36)
    lines.append(f"{'SERVER LOG ANALYSIS REPORT':^36}")
    lines.append("=" * 36)
    lines.append("Log File    : server.log")
    lines.append(f"Lines Read  : {total_lines}")
    lines.append("-" * 36)
    lines.append("SEVERITY COUNTS")

    for level in all_levels:
        count = severity_counts.get(level, 0)
        lines.append(f"  {level:<9}: {count:>4}")

    lines.append("-" * 36)
    lines.append(f"ERROR RATE  : {error_rate:>6.2f}%")
    lines.append("-" * 36)
    lines.append(f"UNIQUE ERRORS ({len(unique_errors)} total)")
    for message in sorted(unique_errors):
        lines.append(f"  - {message}")

    lines.append(f"CRITICAL EVENTS ({len(critical_events)} total)")
    for message in sorted(critical_events):
        lines.append(f"  - {message}")

    lines.append("=" * 36)
    return lines


def write_report(report_lines):
    with open("log_summary.txt", "w") as out:
        for line in report_lines:
            print(line, file=out)


def main():
    severity_counts, unique_errors, critical_events, log_entries = parse_log_file("server.log")
    report_lines = build_report(severity_counts, unique_errors, critical_events, log_entries)
    write_report(report_lines)
    print("log_summary.txt has been created.")
    input("Press Enter to close this window...")


if __name__ == "__main__":
    main()
