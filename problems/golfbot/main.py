N = int(input())
distances = [int(input()) for _ in range(N)]
M = int(input())
holes = [int(input()) for _ in range(M)]

possible_shots = set()
for distance in distances:
    for shot in range(1, 201):
        if distance * shot <= 200:
            possible_shots.add(distance * shot)

count = 0
for hole in holes:
    if hole in possible_shots:
        count += 1

print(count)