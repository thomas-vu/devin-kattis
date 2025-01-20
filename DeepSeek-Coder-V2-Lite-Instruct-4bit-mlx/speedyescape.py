import sys
from math import sqrt, inf
from heapq import heappush, heappop

def read_ints():
    return list(map(int, input().split()))

n, m, e = read_ints()
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, l = read_ints()
    edges[a].append((b, l))
    edges[b].append((a, l))

exits = set(read_ints())
start_b, start_p = read_ints()

def dijkstra(start):
    dist = [inf] * (n + 1)
    pq = [(0, start)]
    dist[start] = 0
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, l in edges[u]:
            if dist[v] > dist[u] + l:
                dist[v] = dist[u] + l
                heappush(pq, (dist[v], v))
    return dist

dist_b = dijkstra(start_b)
dist_p = dijkstra(start_p)

min_speed = inf
for exit in exits:
    if dist_b[exit] < dist_p[exit]:
        min_speed = min(min_speed, (dist_b[exit] * 3600) / 1000)

if min_speed == inf:
    print("IMPOSSIBLE")
else:
    print(f"{min_speed:.10f}")