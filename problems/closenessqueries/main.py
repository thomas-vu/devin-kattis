import sys
import random
from collections import deque

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
Q = int(sys.stdin.readline())
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]

# Create adjacency list from edges
adj_list = [[] for _ in range(N)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Function to perform BFS and find shortest path between two nodes
def bfs(start, end):
    visited = [False] * N
    queue = deque([(start, 0)])
    visited[start] = True
    
    while queue:
        node, dist = queue.popleft()
        
        if node == end:
            return dist
        
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))
    
    return -1

# Process each query and print the result
for u, v in queries:
    dist = bfs(u, v)
    print(dist)