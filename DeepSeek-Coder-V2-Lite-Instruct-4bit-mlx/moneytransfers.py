import sys
import heapq

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def read_graph(N, P):
    graph = {i: [] for i in range(1, N + 1)}
    for _ in range(P):
        a, b, c = read_ints()
        graph[a].append((b, c))
        graph[b].append((a, c))
    return graph

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
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
    return dist

def solve():
    N, P, X, Y = read_ints()
    graph = read_graph(N, P)
    SWERC_banks = set(read_ints())
    
    if X not in SWERC_banks or Y not in SWERC_banks:
        print("Impossible")
        return
    
    dist_X = dijkstra(graph, X)
    dist_Y = dijkstra(graph, Y)
    
    min_cost = float('inf')
    for bank in SWERC_banks:
        if bank != X and bank != Y:
            min_cost = min(min_cost, dist_X[bank] + dist_Y[bank])
    
    if min_cost == float('inf'):
        print("Impossible")
    elif min_cost == 0:
        print("Infinity")
    else:
        max_fee = (dist_X[Y] - min_cost) // 2
        print(max_fee)

solve()