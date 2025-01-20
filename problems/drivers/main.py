import sys
from collections import defaultdict, deque

def can_deliver(N, roads, queries, p):
    graph = defaultdict(list)
    for x, y, t in roads:
        graph[x].append((y, t))
        graph[y].append((x, t))
    
    def bfs(start, end, max_drive_time):
        visited = [False] * (N + 1)
        queue = deque([(start, max_drive_time)])
        visited[start] = True
        
        while queue:
            city, time_left = queue.popleft()
            
            if city == end:
                return True
            
            for neighbor, travel_time in graph[city]:
                if not visited[neighbor] and time_left >= travel_time:
                    visited[neighbor] = True
                    queue.append((neighbor, time_left - travel_time))
        
        return False
    
    results = []
    for a, b, p in queries:
        if bfs(a, b, p):
            results.append("TAIP")
        else:
            results.append("NE")
    
    return results

# Read input
N, M, U = map(int, sys.stdin.readline().split())
roads = [tuple(map(int, sys.stdin.readline().split())) for _ in range(M)]
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(U)]

# Process queries and output results
results = can_deliver(N, roads, queries, p)
for result in results:
    print(result)