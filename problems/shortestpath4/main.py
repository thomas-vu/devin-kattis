# This code defines a function to solve the given problem using Dijkstra's algorithm with limited edges
import heapq

def dijkstra(graph, start, dest, k):
    n = len(graph)
    dist = [[float('inf')] * (k + 1) for _ in range(n)]
    dist[start][0] = 0
    pq = [(0, start, 0)]  # (distance, vertex, edges used)
    
    while pq:
        d, u, e = heapq.heappop(pq)
        
        if u == dest:
            return d
        
        if d > dist[u][e]:
            continue
        
        for v, w in graph[u]:
            if e + 1 <= k and d + w < dist[v][e + 1]:
                for i in range(e + 2, k + 1):
                    if d + w < dist[v][i]:
                        dist[v][i] = d + w
                        heapq.heappush(pq, (d + w, v, i))
                dist[v][e + 1] = d + w
                heapq.heappush(pq, (d + w, v, e + 1))
    
    return -1

def main():
    TC = int(input())
    for _ in range(TC):
        V = int(input())
        graph = [[] for _ in range(V)]
        for i in range(V):
            data = list(map(int, input().split()))
            X = data[0]
            for j in range(1, X + 1, 2):
                v = data[j]
                w = data[j + 1]
                graph[i].append((v, w))
        
        Q = int(input())
        for _ in range(Q):
            s, t, k = map(int, input().split())
            result = dijkstra(graph, s, t, k)
            print(result)
        if _ < TC - 1:
            input()  # Consume the newline after each test case

if __name__ == "__main__":
    main()