import heapq

def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if u == end:
            break
        for v, w in graph[u]:
            if dist[v] > d + max(0, h[v] - h[u]):
                dist[v] = d + max(0, h[v] - h[u])
                heapq.heappush(pq, (dist[v], v))
    
    return dist[end]

# Read input
N, M = map(int, input().split())
start, end = map(int, input().split())
h = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    graph[i-1].append((j-1, max(0, h[i-1] - h[j-1])))
    graph[j-1].append((i-1, max(0, h[j-1] - h[i-1])))

# Run Dijkstra's algorithm
result = dijkstra(graph, start-1, end-1)
print(result)