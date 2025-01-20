# The solution to the given problem is as follows:

import sys
from collections import defaultdict, deque

# Read input
V, E = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(E):
    a, b = map(int, sys.stdin.readline().split())
    edges[a].append(b)

# Topological sort to find the longest path in a DAG
in_degree = [0] * (V + 1)
for node in edges:
    for neighbor in edges[node]:
        in_degree[neighbor] += 1

queue = deque([i for i in range(1, V + 1) if in_degree[i] == 0])
longest_path = []

while queue:
    node = queue.popleft()
    longest_path.append(node)
    for neighbor in edges[node]:
        in_degree[neighbor] -= 1
        if in_degree[neighbor] == 0:
            queue.append(neighbor)

# Output the result
print(len(longest_path))
print(' '.join(map(str, longest_path)))