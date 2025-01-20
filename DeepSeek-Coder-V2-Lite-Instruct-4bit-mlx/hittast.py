import heapq

def dijkstra(graph, start, n):
    dist = [[float('inf')] * (n + 1) for _ in range(2)]
    dist[0][start] = 0
    pq = [(0, start, 0)]
    
    while pq:
        d, u, typ = heapq.heappop(pq)
        
        if d > dist[typ][u]:
            continue
        
        for v, cost in graph[u]:
            new_cost = d + cost
            if new_cost < dist[typ][v]:
                dist[typ][v] = new_cost
                heapq.heappush(pq, (new_cost, v, typ))
            if typ == 0:
                new_cost_alt = d + cost + min(dist[1][v], dist[0][v])
                if new_cost_alt < dist[1][v]:
                    dist[1][v] = new_cost_alt
                    heapq.heappush(pq, (new_cost_alt, v, 1))
    
    return min(dist[0][n], dist[1][n])

# Read input
n, m = map(int, input().split())
lodging_costs = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

# Read travel options
for _ in range(m):
    u, v, a, b = map(int, input().split())
    graph[u].append((v, a))
    graph[v].append((u, b))

# Run Dijkstra's algorithm for both Álfur and Benedikt
result = dijkstra(graph, 1, n)
print(result)