import sys
from heapq import heappush, heappop

def dijkstra(graph, start):
    n = len(graph)
    dist = [sys.maxsize] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v in range(n):
            if graph[u][v] != 0:
                new_dist = dist[u] + graph[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heappush(pq, (new_dist, v))
    return dist

# Read input
N, S, T = map(int, sys.stdin.readline().strip().split())
graph = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

# Run Dijkstra's algorithm from the starting intersection
distances = dijkstra(graph, S)

# Output the minimum time to reach the meeting point
print(distances[T])