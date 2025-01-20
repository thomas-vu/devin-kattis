import sys
from collections import defaultdict, deque

MOD = 10**9 + 7

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def main():
    j, b = read_ints()
    graph = defaultdict(list)
    
    for _ in range(b):
        u, v, l = read_ints()
        graph[u].append((v, l))
        graph[v].append((u, l))
    
    # Dijkstra's algorithm to find shortest paths from junction 0
    dist = [float('inf')] * j
    dist[0] = 0
    ways = [0] * j
    ways[0] = 1
    pq = [(0, 0)]
    
    while pq:
        d, u = min(pq)
        pq.remove((d, u))
        
        if d > dist[u]:
            continue
        
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                ways[v] = ways[u]
                pq.append((dist[v], v))
            elif dist[v] == d + w:
                ways[v] = (ways[v] + ways[u]) % MOD
    
    # Output the number of unique routes through each junction
    for i in range(j):
        print(ways[i] if ways[i] != 0 else -1)

if __name__ == "__main__":
    main()