def minimum_range(n, m, roads):
    if m == 0:
        return "IMPOSSIBLE"
    
    # Create adjacency list for the graph
    adj_list = {i: [] for i in range(n)}
    for u, v, w in roads:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))
    
    # Perform Dijkstra's algorithm to find the shortest paths between all pairs of cities
    import heapq
    dist = [[float('inf')] * n for _ in range(n)]
    
    def dijkstra(start):
        pq = [(0, start)]
        dist[start][start] = 0
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[start][u]:
                continue
            for v, w in adj_list[u]:
                if d + w < dist[start][v]:
                    dist[start][v] = d + w
                    heapq.heappush(pq, (d + w, v))
    
    for i in range(n):
        dijkstra(i)
    
    # Find the maximum distance between any two cities
    max_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            max_distance = max(max_distance, dist[i][j])
    
    return max_distance if max_distance != float('inf') else "IMPOSSIBLE"

# Read input
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
roads = []
for _ in range(m):
    u = int(data[index])
    v = int(data[index + 1])
    w = int(data[index + 2])
    roads.append((u, v, w))
    index += 3

# Output the result for each road network
print(minimum_range(n, m, roads))