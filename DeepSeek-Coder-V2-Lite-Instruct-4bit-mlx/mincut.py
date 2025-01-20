import sys
from heapq import heappush, heappop

def min_cut(n, m, s, t, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
    
    def dijkstra(source):
        dist = [float('inf')] * n
        dist[source] = 0
        heap = [(0, source)]
        while heap:
            d, u = heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heappush(heap, (dist[v], v))
        return dist
    
    dist_s = dijkstra(s)
    dist_t = dijkstra(t)
    
    min_weight = float('inf')
    best_set = set()
    
    for u in range(n):
        if dist_s[u] + dist_t[u] == dist_s[t]:
            for v, w in graph[u]:
                if dist_s[u] + w == dist_s[v] and w < min_weight:
                    min_weight = w
                    best_set = {u}
    
    return best_set

# Read input
n, m, s, t = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

# Process the input and output the result
U = min_cut(n, m, s, t, edges)
print(len(U))
for u in U:
    print(u)