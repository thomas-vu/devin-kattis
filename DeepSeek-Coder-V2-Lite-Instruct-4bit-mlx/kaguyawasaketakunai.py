import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heappush(heap, (dist[v], v))
    return dist

def main():
    N, E, s, d = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    edges = []
    
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
        edges.append((u, v, w))
    
    original_dist = dijkstra(graph, s)
    target_dist = dijkstra(graph, d)
    
    min_operations = target_dist[s] - 1
    increase = [0] * (N + 1)
    
    for i in range(E):
        u, v, w = edges[i]
        if original_dist[u] + 1 == target_dist[v]:
            increase[u] += 1
        elif original_dist[v] + 1 == target_dist[u]:
            increase[v] += 1
    
    print(min_operations)
    for u, v, w in edges:
        if increase[u] > 0 and original_dist[u] + increase[u] == target_dist[v]:
            print(u, v, increase[u])
        elif increase[v] > 0 and original_dist[v] + increase[v] == target_dist[u]:
            print(v, u, increase[v])

if __name__ == "__main__":
    main()