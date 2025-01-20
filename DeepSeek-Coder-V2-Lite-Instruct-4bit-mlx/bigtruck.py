import heapq

def dijkstra(graph, n):
    pq = [(0, 1)]  # (distance, location)
    distances = [float('inf')] * (n + 1)
    distances[1] = 0
    items_picked_up = [0] * (n + 1)
    heapq.heappush(pq, (0, 1))
    
    while pq:
        dist, loc = heapq.heappop(pq)
        if dist > distances[loc]:
            continue
        
        for neighbor, road_len in graph[loc]:
            new_dist = dist + road_len
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
                items_picked_up[neighbor] = items_picked_up[loc] + t[neighbor - 1]
    
    return distances, items_picked_up

# Read input
n = int(input())
t = list(map(int, input().split()))
m = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b, d = map(int, input().split())
    graph[a].append((b, d))
    graph[b].append((a, d))

# Run Dijkstra's algorithm
distances, items_picked_up = dijkstra(graph, n)

if distances[n] == float('inf'):
    print("impossible")
else:
    print(distances[n], items_picked_up[n])