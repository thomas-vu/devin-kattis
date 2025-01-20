n = int(input())
roads = [list(map(int, input().split())) for _ in range(n)]

# Create a list to store the assignment of roads to cities
city_assignments = [[] for _ in range(n)]

# Assign roads to cities based on the input
for i, (a, b) in enumerate(roads):
    city_assignments[a - 1].append((a, b))
    city_assignments[b - 1].append((a, b))

# Output the assignment of roads to cities
for assignments in city_assignments:
    for road in assignments:
        print(*road)