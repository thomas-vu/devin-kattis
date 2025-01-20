n = int(input())
log_entries = [input().split() for _ in range(n)]
statuses = {}
for entry in log_entries:
    name, action = entry[0], entry[1]
    if name not in statuses:
        statuses[name] = 0
    if action == 'enter':
        if statuses[name] == 0:
            print(f"{name} entered")
            statuses[name] = 1
        else:
            print(f"{name} entered (ANOMALY)")
    elif action == 'exit':
        if statuses[name] == 1:
            print(f"{name} exited")
            statuses[name] = 0
        else:
            print(f"{name} exited (ANOMALY)")