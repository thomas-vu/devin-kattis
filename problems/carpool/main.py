import sys
from heapq import heappush, heappop

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    return dist

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n + 2)]
    
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    dist_campus = dijkstra(graph, 0)
    dist_joes = dijkstra(graph, n + 1)
    
    min_time = float('inf')
    for i in range(n):
        time = max(dist_campus[i], dist_joes[i]) + 5 * (n - i)
        min_time = min(min_time, time)
    
    print(min_time)

if __name__ == "__main__":
    main()