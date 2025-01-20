import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 1.0
    pq = [(dist[start], start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, factor in graph[u]:
            new_dist = d * factor
            if new_dist > dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))
    return dist[n-1]

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        graph = [[] for _ in range(n)]
        for _ in range(m):
            x, y, f = map(float, input().split())
            graph[x].append((y, f))
            graph[y].append((x, f))
        result = dijkstra(graph, 0)
        print("{:.4f}".format(result))

if __name__ == "__main__":
    main()