import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heappush(pq, (dist[v], v))
    return dist, prev

def find_path(prev, start, end):
    path = []
    while end != -1:
        path.append(end)
        end = prev[end]
    return list(reversed(path))

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    dist, prev = dijkstra(graph, 0)
    
    if dist[1] == float('inf'):
        print("impossible")
    else:
        path = find_path(prev, 0, 1)
        print(len(path), end=' ')
        print(*path)

if __name__ == "__main__":
    main()