import sys
INF = float('inf')

def bellman_ford(n, edges, start):
    dist = [INF] * n
    dist[start] = 0
    for _ in range(n - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    return dist

def process_queries(n, edges, queries):
    for u, v in queries:
        dist = bellman_ford(n, edges, u)
        if dist[v] == INF:
            print("Impossible")
        elif dist[v] == -INF:
            print("-Infinity")
        else:
            print(dist[v])

def main():
    while True:
        n, m, q = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0 and q == 0:
            break
        edges = []
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            edges.append((u, v, w))
        queries = []
        for _ in range(q):
            u, v = map(int, sys.stdin.readline().split())
            queries.append((u, v))
        process_queries(n, edges, queries)
        print()

if __name__ == "__main__":
    main()