import sys
from collections import defaultdict, deque

# Read input
n, m, p, g = map(int, sys.stdin.readline().split())
starts = list(map(int, sys.stdin.readline().split()))
connections = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    connections[a].append((b, c))
    connections[b].append((a, c))

# BFS to find shortest paths from each station to the idyllic village (station 1)
distances = {i: float('inf') for i in range(1, n + 1)}
distances[1] = 0
queue = deque([1])
while queue:
    current = queue.popleft()
    for neighbor, weight in connections[current]:
        if distances[neighbor] > distances[current] + weight:
            distances[neighbor] = distances[current] + weight
            queue.append(neighbor)

# Calculate the total cost for each family member based on individual or group tickets
total_cost = 0
for start in starts:
    shortest_distance = distances[start]
    if shortest_distance * g < p * g:  # Use individual ticket if cheaper
        total_cost += shortest_distance
    else:  # Otherwise, use group ticket
        total_cost += p * g

# Output the total cost
print(total_cost)