from itertools import permutations
import sys

def read_ints():
    return list(map(int, input().split()))

# Read the number of intersections and roads
N, M = read_ints()

# Read the road connections
roads = [list(read_ints()) for _ in range(M)]

# Read the number of stores
S = int(input())
stores = [int(input()) for _ in range(S)]

# Create a graph from the roads
graph = {i: [] for i in range(N)}
for x, y, d in roads:
    graph[x].append((y, d))
    graph[y].append((x, d))

# Use Dijkstra's algorithm to find the shortest paths from the house to all stores
def dijkstra(start):
    dist = [float('inf')] * N
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = min(pq)
        pq.remove((d, u))
        for v, w in graph[u]:
            if d + w < dist[v]:
                pq.remove((dist[v], v))
                dist[v] = d + w
                pq.append((dist[v], v))
    return dist

# Calculate the shortest path to all stores from the house
dist_from_house = dijkstra(0)

# Calculate the shortest path between each pair of stores and back to the house
min_trip = float('inf')
for perm in permutations(stores):
    trip_dist = 0
    for i in range(S - 1):
        trip_dist += dijkstra(perm[i])[perm[i + 1]]
    trip_dist += dijkstra(perm[-1])[0] + dist_from_house[perm[0]]
    min_trip = min(min_trip, trip_dist)

# Output the shortest possible shopping trip
print(min_trip)