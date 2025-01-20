import heapq

def dijkstra(graph, n, s):
    dist = [float('inf')] * n
    dist[s] = 0
    pq = [(0, s)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, t0, P, w in graph[u]:
            if dist[u] % P + t0 < t0:
                nt = (t0 - dist[u] % P) + t0
            else:
                nt = (t0 - dist[u] % P) + t0 + P
            if dist[u] + nt < dist[v]:
                dist[v] = dist[u] + nt + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def main():
    while True:
        n, m, q, s = map(int, input().split())
        if n == 0 and m == 0 and q == 0 and s == 0:
            break
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, t0, P, d = map(int, input().split())
            graph[u].append((v, t0, P, d))
        dist = dijkstra(graph, n, s)
        for _ in range(q):
            query = int(input())
            if dist[query] == float('inf'):
                print("Impossible")
            else:
                print(dist[query])
        print()

if __name__ == "__main__":
    main()