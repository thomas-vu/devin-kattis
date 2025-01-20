import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [None] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    M = int(data[index + 1])
    index += 2
    
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        w = int(data[index + 2])
        graph[u].append((v, w))
        index += 3
    
    s = int(data[index])
    t = int(data[index + 1])
    
    dist_s, _ = dijkstra(graph, s)
    _, prev_t = dijkstra(graph, t)
    
    candidates = set()
    current = t
    while current is not None:
        candidates.add(current)
        current = prev_t[current]
    
    result = []
    for u in candidates:
        if dist_s[u] + dist_s[t] == dist_s[t]:
            result.append(u)
    
    print(' '.join(map(str, sorted(result))))

if __name__ == "__main__":
    main()