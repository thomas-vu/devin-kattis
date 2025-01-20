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

def main():
    n = int(input())
    x = int(input())
    bike_paths = [list(map(int, input().split())) for _ in range(x)]
    y = int(input())
    non_bike_paths = [list(map(int, input().split())) for _ in range(y)]
    z = int(input())
    locations_to_visit = list(map(int, input().split()))
    
    # Create graph for bike paths and non-bike paths
    bike_graph = [[] for _ in range(n)]
    non_bike_graph = [[] for _ in range(n)]
    
    for u, v, t in bike_paths:
        bike_graph[u].append((v, t))
        bike_graph[v].append((u, t))
    
    for u, v, t in non_bike_paths:
        non_bike_graph[u].append((v, t))
        non_bike_graph[v].append((u, t))
    
    # Calculate shortest paths from each location to all others using both bike and non-bike paths
    dist_bike = [dijkstra(bike_graph, i) for i in range(n)]
    dist_non_bike = [dijkstra(non_bike_graph, i) for i in range(n)]
    
    # Initialize DP array to store minimum time to reach each location with the bike
    dp = [[float('inf')] * (z + 1) for _ in range(n)]
    dp[0][0] = 0
    
    # Use DP to find the minimum time to reach each location with the bike and switch back to non-bike if necessary
    for i in range(z):
        for j in range(n):
            if dp[j][i] != float('inf'):
                # Stay at the current location with the bike
                dp[j][i + 1] = min(dp[j][i + 1], dp[j][i] + dist_bike[j][locations_to_visit[i]])
                # Switch to non-bike and travel to the next location
                for k in range(n):
                    if j != k:
                        dp[k][i + 1] = min(dp[k][i + 1], dp[j][i] + dist_non_bike[j][k] + dist_bike[k][locations_to_visit[i]])
    
    # Find the minimum time to return home with the bike after visiting all locations
    result = float('inf')
    for i in range(n):
        result = min(result, dp[i][z] + dist_bike[i][0])
    
    print(result)

if __name__ == "__main__":
    main()