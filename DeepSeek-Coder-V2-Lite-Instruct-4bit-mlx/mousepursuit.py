n = int(input())
cheese_gained = 0
glory_gained = 0
events = []
for _ in range(n):
    event = input().split()
    if event[0] == 'CAUGHT':
        s, c, g = int(event[1]), int(event[2]), int(event[3])
        events.append((s, c, g))
    else:
        s, c, g = int(event[1]), -int(event[2]), -int(event[3])
        events.append((s, c, g))
k = int(input())
for e in events:
    if e[0] <= k:
        cheese_gained += e[1]
        glory_gained += e[2]
print(cheese_gained, glory_gained)