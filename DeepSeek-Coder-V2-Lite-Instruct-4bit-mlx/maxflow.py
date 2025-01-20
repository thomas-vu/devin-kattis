import sys
from collections import deque, defaultdict

input = sys.stdin.read
data = input().split()
index = 0

def read_ints():
    global index
    values = []
    while index < len(data):
        values.append(int(data[index]))
        index += 1
    return values

# Read input
n, m, s, t = read_ints()
edges = []
graph = defaultdict(list)
capacity = {}
for _ in range(m):
    u, v, c = read_ints()
    edges.append((u, v))
    graph[u].append(v)
    capacity[(u, v)] = c

# Ford-Fulkerson algorithm for maximum flow
def bfs(start, target, graph, capacity):
    queue = deque([start])
    parent = {start: None}
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if v not in parent and capacity.get((u, v), 0) > 0:
                parent[v] = u
                queue.append(v)
                if v == target:
                    break
    path = []
    current = t
    while parent[current] is not None:
        path.append((parent[current], current))
        current = parent[current]
    return path[::-1]

# Find maximum flow
max_flow = 0
while True:
    path = bfs(s, t, graph, capacity)
    if not path:
        break
    min_capacity = float('inf')
    for u, v in path:
        min_capacity = min(min_capacity, capacity.get((u, v), 0))
    for u, v in path:
        capacity[(u, v)] -= min_capacity
        if (v, u) not in capacity:
            graph[v].append(u)
        capacity[(v, u)] = min_capacity
    max_flow += min_capacity

# Reconstruct the flow graph from the edges with non-zero capacity
flow_graph = defaultdict(list)
for u, v in edges:
    if capacity.get((u, v), 0) > 0:
        flow_graph[u].append(v)
edges = []
for u, v in capacity:
    if capacity[(u, v)] > 0:
        edges.append((u, v, capacity[(u, v)]))

# Output the result
print(f"{n} {max_flow} {len(edges)}")
for u, v, c in edges:
    print(f"{u} {v} {c}")