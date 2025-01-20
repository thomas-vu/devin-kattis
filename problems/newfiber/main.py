import sys
from collections import defaultdict, deque

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# Create adjacency list for the original graph
adj = defaultdict(list)
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

# Create adjacency list for the new graph with wireless links
new_edges = []

# Find nodes that need to change their number of connections
changes = set()
for node in range(n):
    if len(adj[node]) != sum([len(adj[neighbor]) for neighbor in adj[node]]):
        changes.add(node)

# BFS to check connectivity and build the new graph
visited = [False] * n
queue = deque()
for node in changes:
    visited[node] = True
    queue.append(node)
    
while queue:
    node = queue.popleft()
    for neighbor in adj[node]:
        if not visited[neighbor]:
            new_edges.append((node, neighbor))
            visited[neighbor] = True
            queue.append(neighbor)

# Output the result
print(len(changes))
for a, b in new_edges:
    print(a, b)