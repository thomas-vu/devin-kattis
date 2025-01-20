from collections import defaultdict, deque
import sys

# Read input
N, M, alpha = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(M):
    u, v, c = map(int, sys.stdin.readline().split())
    edges[u].append((v, c))
    edges[v].append((u, c))

# BFS to find the shortest path in terms of roads
def bfs(start):
    visited = [False] * (N + 1)
    queue = deque([(start, -1)])
    visited[start] = True
    while queue:
        node, parent_edge = queue.popleft()
        for neighbor, edge in edges[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, edge))
    return sum(1 for i in visited if i) - 1

# Check all cycles to find the minimum energy cost
min_energy = float('inf')
for start in range(1, N + 1):
    L = K = 0
    candies = defaultdict(int)
    visited_edges = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor, edge in edges[node]:
            if (node, neighbor) not in visited_edges and (neighbor, node) not in visited_edges:
                visited_edges.add((node, neighbor))
                candies[edge] += 1
                K += 1
                queue.append(neighbor)
    if candies:
        L = max(candies.values())
        min_energy = min(min_energy, L**2 + alpha * K)

# Output the result
if min_energy == float('inf'):
    print("Poor girl")
else:
    print(min_energy)