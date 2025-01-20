import sys
from collections import defaultdict, deque

# Read input
n, h = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)
    edges[b].append(a)

# BFS to find the shortest paths from headquarters to all other nodes
def bfs(start):
    visited = [False] * n
    distance = [-1] * n
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    while queue:
        node = queue.popleft()
        for neighbor in edges[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return distance

# Find nodes that are not reachable from the headquarters after blocking one edge
distance_from_headquarters = bfs(h)
not_safe_nodes = [i for i in range(n) if distance_from_headquarters[i] == -1]

# Build a new graph with only the nodes that are not safe after blocking one edge
new_edges = defaultdict(list)
for node in range(n):
    for neighbor in edges[node]:
        if distance_from_headquarters[node] == -1 and distance_from_headquarters[neighbor] == -1:
            new_edges[node].append(neighbor)
            new_edges[neighbor].append(node)

# Find the minimum number of edges to add and which ones to add
to_add = []
for node in not_safe_nodes:
    for neighbor in edges[node]:
        if distance_from_headquarters[neighbor] == -1:
            to_add.append((node, neighbor))

# Output the result
print(len(to_add))
for a, b in to_add:
    print(a, b)