import sys
import heapq

def dijkstra(graph, start, n):
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
            elif dist[v] == d + w:
                continue
    return dist

def process_queries(graph, n, q, s):
    results = []
    for _ in range(q):
        query = int(sys.stdin.readline().strip())
        if dist[query] == float('inf'):
            results.append("Impossible")
        elif dist[query] == float('-inf'):
            results.append("-Infinity")
        else:
            results.append(dist[query])
    return results

while True:
    line = sys.stdin.readline().strip()
    if line == "0 0 0 0":
        break
    n, m, q, s = map(int, line.split())
    graph = {i: [] for i in range(n)}
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        graph[u].append((v, w))
    dist = dijkstra(graph, s, n)
    for _ in range(q):
        query = int(sys.stdin.readline().strip())
        if dist[query] == float('inf'):
            print("Impossible")
        elif dist[query] == float('-inf'):
            print("-Infinity")
        else:
            print(dist[query])
    print()