import sys
from collections import defaultdict, deque

# Read input
P, T = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(T):
    p1, p2, l = map(int, sys.stdin.readline().split())
    edges[p1].append((p2, l))
    edges[p2].append((p1, l))

# BFS to find shortest paths from the entrance (0) to all other points
def bfs(edges, start):
    visited = [False] * P
    distance = [-1] * P
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        u = queue.popleft()
        for v, l in edges[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + l
                queue.append(v)
    return distance

# Find all shortest paths from the entrance to the highest peak (P-1)
shortest_paths = bfs(edges, 0)

# Sum the lengths of all shortest paths to get the total length needed for flowers
total_length = sum(shortest_paths[P-1])

# Output the total length needed for flowers (both sides of the trails)
print(2 * total_length)