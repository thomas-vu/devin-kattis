import heapq

def dijkstra(graph, start, end, capacity):
    n = len(graph)
    pq = [(0, start, 0)]  # (cost, city, fuel)
    dist = [[float('inf')] * (capacity + 1) for _ in range(n)]
    dist[start][0] = 0
    
    while pq:
        cost, u, fuel = heapq.heappop(pq)
        
        if u == end:
            return cost
        
        if fuel < capacity and dist[u][fuel + 1] > cost + graph[u][fuel + 1]:
            dist[u][fuel + 1] = cost + graph[u][fuel + 1]
            heapq.heappush(pq, (dist[u][fuel + 1], u, fuel + 1))
        
        for v, d in graph[u]:
            if fuel >= d and dist[v][fuel - d] > cost:
                dist[v][fuel - d] = cost
                heapq.heappush(pq, (cost, v, fuel - d))
    
    return float('inf')

def main():
    n, m = map(int, input().split())
    prices = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        u, v, d = map(int, input().split())
        graph[u].append((v, d))
        graph[v].append((u, d))
    
    q = int(input())
    for _ in range(q):
        c, s, e = map(int, input().split())
        if c < prices[s]:
            print("impossible")
        else:
            result = dijkstra(graph, s, e, c)
            print(result if result != float('inf') else "impossible")

if __name__ == "__main__":
    main()