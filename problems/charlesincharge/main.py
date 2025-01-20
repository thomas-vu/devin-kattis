import heapq
import sys

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances

def solve():
    input_data = sys.stdin.read().splitlines()
    N, M, X = map(int, input_data[0].split())
    graph = {i: [] for i in range(1, N + 1)}
    edges = []
    for edge_data in input_data[1:]:
        C1, C2, T = map(int, edge_data.split())
        graph[C1].append((C2, T))
        graph[C2].append((C1, T))
        edges.append((C1, C2, T))
    
    shortest_distances = dijkstra(graph, 1)
    shortest_path = shortest_distances[N]
    max_allowed_distance = shortest_path * (1 + X / 100)
    
    min_battery = float('inf')
    for edge in edges:
        C1, C2, T = edge
        graph[C1].remove((C2, T))
        graph[C2].remove((C1, T))
        
        distances_from_start = dijkstra(graph, 1)
        distance_to_N = distances_from_start[N]
        
        max_distance_on_route = 0
        for vertex in range(1, N + 1):
            for neighbor, weight in graph[vertex]:
                max_distance_on_route = max(max_distance_on_route, distances_from_start[vertex] + weight)
        
        min_battery = min(min_battery, max_distance_on_route)
        
        graph[C1].append((C2, T))
        graph[C2].append((C1, T))
    
    print(int(min_battery))

solve()