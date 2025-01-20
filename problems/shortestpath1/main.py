import heapq
import sys

def dijkstra(graph, n, s):
    pq = [(0, s)]
    dist = [float('inf')] * n
    dist[s] = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def main():
    while True:
        n, m, q, s = map(int, sys.stdin.readline().split())
        if n == 0 and m == 0 and q == 0 and s == 0:
            break
        
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u, v, w = map(int, sys.stdin.readline().split())
            graph[u].append((v, w))
        
        dist = dijkstra(graph, n, s)
        
        for _ in range(q):
            t = int(sys.stdin.readline())
            if dist[t] == float('inf'):
                print("Impossible")
            else:
                print(dist[t])
        print()

if __name__ == "__main__":
    main()