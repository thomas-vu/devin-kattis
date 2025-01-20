import heapq
from collections import defaultdict, deque

def dijkstra(graph, start):
    V = len(graph)
    dist = [float('inf')] * V
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def count_shortest_paths(graph, s, t):
    V = len(graph)
    dist = dijkstra(graph, s)
    
    if dist[t] == float('inf'):
        return 0
    
    count = [0] * V
    count[s] = 1
    visited = set([s])
    queue = deque([s])
    
    while queue:
        u = queue.popleft()
        for v, w in graph[u]:
            if dist[v] == dist[u] + w:
                count[v] += count[u]
                if v not in visited:
                    visited.add(v)
                    queue.append(v)
    
    return count[t]

# Read input
V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
s, t = map(int, input().split())

# Calculate and print the number of shortest paths
print(count_shortest_paths(graph, s, t))