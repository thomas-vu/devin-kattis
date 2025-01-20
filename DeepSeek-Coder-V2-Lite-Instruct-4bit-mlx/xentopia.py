import sys
from heapq import heappush, heappop

def dijkstra(graph, start, k1, k2):
    n = len(graph)
    dist = [[sys.maxsize] * (k1 + 1) for _ in range(n)]
    dist[start][0] = 0
    pq = [(0, start, 0)]
    
    while pq:
        d, u, red_used = heappop(pq)
        if u == start and red_used > k1:
            continue
        for v, w, color in graph[u]:
            new_d = d + w
            if color == 1 and red_used < k1:
                new_d = d + w
                if new_d < dist[v][red_used + 1]:
                    for i in range(red_used + 1, k1 + 1):
                        dist[v][i] = new_d
                    heappush(pq, (new_d, v, red_used + 1))
            if color == 2 and red_used <= k1:
                new_d = d + w
                if new_d < dist[v][red_used]:
                    for i in range(red_used, k1 + 1):
                        dist[v][i] = new_d
                    heappush(pq, (new_d, v, red_used))
            if new_d < dist[v][red_used]:
                dist[v][red_used] = new_d
                heappush(pq, (new_d, v, red_used))
    
    min_time = sys.maxsize
    for i in range(k1 + 1):
        min_time = min(min_time, dist[T][i])
    
    return -1 if min_time == sys.maxsize else min_time

# Read input
N, M, k1, k2 = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    U, V, X, C = map(int, sys.stdin.readline().split())
    graph[U].append((V, X, C))
    graph[V].append((U, X, C))
S, T = map(int, sys.stdin.readline().split())

# Run Dijkstra's algorithm
result = dijkstra(graph, S, k1, k2)
print(result)