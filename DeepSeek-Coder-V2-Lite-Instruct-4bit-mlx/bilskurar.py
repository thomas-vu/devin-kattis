n = int(input())
houses = list(map(int, input().split()))
garages = list(map(int, input().split()))

collisions = 0
for i in range(n):
    for j in range(i + 1, n):
        if houses[i] > garages[j] and i < j:
            collisions += 1
        elif houses[i] < garages[j] and i > j:
            collisions += 1

print(collisions)