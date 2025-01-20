def calculate_bill(log):
    total_minutes = 0
    customers = {}
    
    for entry in log:
        if entry.startswith("ENTER"):
            _, name, time = entry.split()
            customers[name] = int(time)
        elif entry.startswith("EXIT"):
            _, name, time = entry.split()
            exit_time = int(time)
            if name in customers:
                total_minutes += (exit_time - customers[name])
                del customers[name]
    
    for name in sorted(customers.keys()):
        total_minutes += (800 - customers[name])
    
    return total_minutes * 0.10

def main():
    logs = []
    while True:
        log_entry = input()
        if log_entry == "CLOSE":
            break
        logs.append(log_entry)
    
    day = 1
    while logs:
        print(f"Day {day}")
        log_entry = logs.pop(0)
        while logs and not logs[0].startswith("OPEN"):
            log_entry += "\n" + logs.pop(0)
        bill = calculate_bill(log_entry.split("\n")[1:-1])
        print("{} ${}".format(next((name for name in customers if customers[name] == log_entry.split("\n")[1:-1][0].split()[1]), "Unknown"), f"{bill:.2f}"))
        customers = {}
        day += 1

if __name__ == "__main__":
    main()