import sys
from collections import defaultdict, deque

# Read input from stdin
N, M = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

# BFS to find the minimum number of IT requests
def min_requests(N, edges):
    if N == 2:
        return 1
    
    visited = [False] * (N + 1)
    queue = deque()
    
    # Start BFS from each unvisited host
    for i in range(1, N + 1):
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            
            while queue:
                node = queue.popleft()
                for neighbor in edges[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            # If there's an unvisited host, we need to add one IT request
            for j in range(1, N + 1):
                if not visited[j]:
                    return 1
    return 0

# Output the result
print(min_requests(N, edges))