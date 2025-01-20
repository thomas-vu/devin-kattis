import sys
import heapq

def read_ints():
    return list(map(int, input().split()))

def dijkstra(n, roads, start):
    graph = {i: [] for i in range(n)}
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
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

def calculate_total_commute_time(n, roads, intersections):
    graph = {i: [] for i in range(n)}
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    total_time = 0
    for i in range(n):
        dist = dijkstra(n, roads, i)
        for j in range(i + 1, n):
            total_time += dist[j]
    return total_time

while True:
    n = int(input())
    if n == 0:
        break
    
    intersections = [read_ints() for _ in range(n)]
    m = int(input())
    roads = [read_ints() for _ in range(m)]
    
    road_map = {}
    for i, (x1, y1) in enumerate(intersections):
        for j, (x2, y2) in enumerate(intersections):
            if i != j:
                road_map[(i, j)] = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    min_reduction = float('inf')
    best_road = None
    
    for (u, v), w in road_map.items():
        new_roads = roads + [(u, v, w)]
        current_time = calculate_total_commute_time(n, new_roads, intersections)
        if current_time < min_reduction:
            min_reduction = current_time
            best_road = (u, v)
    
    if best_road:
        u, v = best_road
        print(f"adding {u} {v} reduces {min_reduction:.10f}")
    else:
        print("no addition reduces")