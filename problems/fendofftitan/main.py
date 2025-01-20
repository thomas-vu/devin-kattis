from heapq import heappop, heappush

def dijkstra(graph, start, end):
    N = len(graph)
    dist = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    dist[start][0] = 0
    heap = [(0, start, 0)]  # (distance, node, shaman_count)
    
    while heap:
        d, u, s = heappop(heap)
        
        if u == end:
            return d, s
        
        for v, w, c in graph[u]:
            new_d = d + w
            new_s = s + (c == 1) + (c == 2)
            
            if new_d < dist[v][new_s]:
                dist[v][new_s] = new_d
                heappush(heap, (new_d, v, new_s))
    
    return float('inf'), N  # IMPOSSIBLE

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    M = int(data[index + 1])
    X = int(data[index + 2])
    Y = int(data[index + 3])
    
    graph = [[] for _ in range(N + 1)]
    index += 4
    
    for _ in range(M):
        A = int(data[index])
        B = int(data[index + 1])
        W = int(data[index + 2])
        C = int(data[index + 3])
        graph[A].append((B, W, C))
        graph[B].append((A, W, C))
        index += 4
    
    dist, shaman_count = dijkstra(graph, X, Y)
    
    if dist == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(dist, shaman_count, dist - shaman_count * 2)

if __name__ == "__main__":
    main()