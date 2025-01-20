import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
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

def min_cost_with_flight(n, roads, flights, s, t):
    graph = [[] for _ in range(n)]
    for i, j, c in roads:
        graph[i].append((j, c))
        graph[j].append((i, c))
    
    flight_graph = [[] for _ in range(n)]
    for u, v in flights:
        flight_graph[u].append(v)
    
    # Run Dijkstra's algorithm from start city s without using the flight ticket
    dist_no_flight = dijkstra(graph, s)
    
    # Run Dijkstra's algorithm from start city s using the flight ticket optimally
    dist_with_flight = [float('inf')] * n
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist_with_flight[u]:
            continue
        for v in flight_graph[u]:
            if dist_with_flight[v] > d + min(dist_no_flight[u], dist_no_flight[v]):
                dist_with_flight[v] = d + min(dist_no_flight[u], dist_no_flight[v])
                heapq.heappush(pq, (dist_with_flight[v], v))
    
    return dist_with_flight[t] if dist_with_flight[t] != float('inf') else -1

# Read input
n, m, f, s, t = map(int, input().split())
roads = []
for _ in range(m):
    i, j, c = map(int, input().split())
    roads.append((i, j, c))
flights = []
for _ in range(f):
    u, v = map(int, input().split())
    flights.append((u, v))

# Output the minimum cost
print(min_cost_with_flight(n, roads, flights, s, t))