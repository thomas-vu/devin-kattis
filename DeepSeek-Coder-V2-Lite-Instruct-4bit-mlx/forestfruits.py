import sys
from heapq import heappop, heappush

def dijkstra(graph, start):
    V = len(graph)
    dist = [float('inf')] * V
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
    V, E, C, K, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    fruit_clearings = list(map(int, sys.stdin.readline().split()))
    
    # Check if all fruit clearings can be reached from the cottage
    dist_from_cottage = dijkstra(graph, 1)
    reachable = all(dist_from_cottage[f] < float('inf') for f in fruit_clearings)
    
    if not reachable:
        print(-1)
        return
    
    min_distance = float('inf')
    for f in fruit_clearings:
        # Calculate the distance to this clearing and back
        dist_to_f = dist_from_cottage[f]
        # Calculate the next fruit available date
        next_fruit_available = (M - dist_to_f) // K + 1
        # Calculate the total distance for this clearing on day M
        dist_to_cottage = dijkstra(graph, f)[1]
        total_distance = dist_to_f + (next_fruit_available - 1) * dist_to_cottage
        min_distance = min(min_distance, total_distance)
    
    print(min_distance)

if __name__ == "__main__":
    main()