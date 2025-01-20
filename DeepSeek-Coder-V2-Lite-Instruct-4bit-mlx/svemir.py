import heapq
from collections import defaultdict

def read_ints():
    return list(map(int, input().split()))

N = int(input())
planets = [read_ints() for _ in range(N)]

edges = defaultdict(list)
for i in range(N):
    for j in range(i + 1, N):
        cost = min(abs(planets[i][0] - planets[j][0]), abs(planets[i][1] - planets[j][1]), abs(planets[i][2] - planets[j][2]))
        edges[i].append((cost, j))
        edges[j].append((cost, i))

visited = [False] * N
total_cost = 0
min_heap = [(0, 0)]
while min_heap:
    cost, u = heapq.heappop(min_heap)
    if visited[u]:
        continue
    visited[u] = True
    total_cost += cost
    for neighbor_cost, v in edges[u]:
        if not visited[v]:
            heapq.heappush(min_heap, (neighbor_cost, v))

print(total_cost)