import sys
from collections import defaultdict, deque

# Read input
n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(m):
    u, v, d = map(int, sys.stdin.readline().split())
    graph[u].append((v, d))
    graph[v].append((u, d))

# BFS to find shortest path from cabin 0 to cabin n-1
def bfs_shortest_path(graph, start):
    visited = [False] * n
    distance = [-1] * n
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        current = queue.popleft()
        for neighbor, edge_len in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + edge_len
                queue.append(neighbor)
    
    return distance[n-1]

# Calculate the shortest path length from 0 to n-1
shortest_path = bfs_shortest_path(graph, 0)

# Calculate the number of hours Dr. Knight needs to wait
if shortest_path == -1:
    print(0)
else:
    # Dr. Knight's travel time is the shortest path length
    knight_travel_time = shortest_path
    
    # Mr. Day's travel time is 12 hours per day until he reaches the destination
    if shortest_path % 12 == 0:
        mr_day_travel_time = shortest_path
    else:
        # Calculate the number of days Mr. Day needs to reach the destination
        mr_day_travel_time = (shortest_path // 12 + 1) * 12
    
    # Calculate the waiting time for Dr. Knight
    waiting_time = mr_day_travel_time - knight_travel_time
    print(waiting_time)