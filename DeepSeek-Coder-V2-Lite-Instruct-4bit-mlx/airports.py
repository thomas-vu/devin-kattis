def min_planes(n, m, inspection_times, flight_times, flights):
    from collections import defaultdict
    import heapq

    # Create adjacency list for the graph
    adj_list = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j:
                adj_list[i].append((j, flight_times[i][j]))

    # Dijkstra's algorithm to find shortest paths from each airport
    def dijkstra(start):
        dist = [float('inf')] * n
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in adj_list[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    # Calculate shortest paths from each airport
    all_distances = [dijkstra(i) for i in range(n)]

    # Create a graph where nodes are flights and edges have weights based on inspection times
    flight_graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i != j:
                flight_graph[i].append((j, all_distances[i][j] + inspection_times[j]))

    # Use Dijkstra's algorithm to find the minimum number of planes needed
    start_times = defaultdict(lambda: float('inf'))
    for s, f, t in flights:
        start_times[s] = min(start_times[s], t)
    pq = [(0, s, start_times[s]) for s in range(1, n + 1)]
    heapq.heapify(pq)
    while pq:
        cost, u, start_time = heapq.heappop(pq)
        if u == f:
            return cost + 1
        for v, w in flight_graph[u]:
            new_start_time = max(start_time, w) + inspection_times[v]
            heapq.heappush(pq, (cost + 1, v, new_start_time))
    return n

# Read input
n, m = map(int, input().split())
inspection_times = list(map(int, input().split()))
flight_times = [list(map(int, input().split())) for _ in range(n)]
flights = [list(map(int, input().split())) for _ in range(m)]

# Output the result
print(min_planes(n, m, inspection_times, flight_times, flights))