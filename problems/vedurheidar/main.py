v = int(input())
n = int(input())
roads = []
for _ in range(n):
    s, k = input().split()
    roads.append((s, int(k)))

for road in roads:
    if road[1] >= v:
        print(f"{road[0]} opin")
    else:
        print(f"{road[0]} lokud")