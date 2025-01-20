import sys
from collections import defaultdict, deque

# Read input
n, m = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(m):
    a, b, t = map(int, sys.stdin.readline().split())
    edges[a].append((b, t))
    edges[b].append((a, t))
dragon_balls = list(map(int, sys.stdin.readline().split()))

# Perform BFS to find the minimum cost to collect all Dragon Balls
def bfs_collect_balls(start):
    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True
    total_cost = 0
    collected_balls = set()

    while queue:
        city, cost = queue.popleft()
        total_cost += cost
        
        # Collect Dragon Balls in the current city
        if city in dragon_balls:
            collected_balls.add(city)
        
        # If all Dragon Balls are collected, return the total cost
        if len(collected_balls) == 7:
            return total_cost
        
        # Explore neighbors
        for neighbor, edge_cost in edges[city]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, edge_cost))
    
    return -1

# Start BFS from city 1
result = bfs_collect_balls(1)
print(result)