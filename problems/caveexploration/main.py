# Python code to solve the problem
from collections import defaultdict, deque
import sys

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS to find all nodes that can reach node 0
def bfs(graph, start):
    visited = [False] * N
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return [i for i in range(N) if visited[i]]

# Find all nodes that can reach node 0
reachable_nodes = bfs(graph, 0)
# Calculate the number of safe junctions
safe_junctions = N - len(reachable_nodes)
# Output the result
print(safe_junctions)