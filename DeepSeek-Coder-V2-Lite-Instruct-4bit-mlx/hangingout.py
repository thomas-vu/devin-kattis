L, x = map(int, input().split())
denied_entries = 0
current_people = 0

for _ in range(x):
    event, p = input().split()
    p = int(p)
    
    if event == "enter":
        if current_people + p > L:
            denied_entries += 1
        else:
            current_people += p
    elif event == "leave":
        current_people -= p

print(denied_entries)