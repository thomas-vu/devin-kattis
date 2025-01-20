import sys
from collections import defaultdict, deque

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = []
graph = defaultdict(list)
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c, i))
    graph[a].append(i)
    graph[b].append(i)

# BFS to find the path with maximum capacity
def bfs_with_capacity(graph, edges):
    queue = deque([0])
    visited = set()
    path_edges = []
    while queue:
        current = queue.popleft()
        if current == n - 1:
            break
        for edge_id in graph[current]:
            if edge_id not in visited:
                a, b, c, i = edges[edge_id]
                if current == a:
                    next_intersection = b
                else:
                    next_intersection = a
                path_edges.append(edge_id)
                queue.append(next_intersection)
                visited.add(edge_id)
    return path_edges, visited

# Find the streets to block
path_edges, visited = bfs_with_capacity(graph, edges)
to_block = []
for edge_id in range(m):
    if edge_id not in visited:
        to_block.append(str(edge_id))

# Output the result
if not to_block:
    print("none")
else:
    print(' '.join(to_block))