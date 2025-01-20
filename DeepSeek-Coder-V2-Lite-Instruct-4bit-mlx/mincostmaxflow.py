import sys
from collections import deque, defaultdict

# Read input
n, m, s, t = map(int, sys.stdin.readline().split())
edges = []
graph = defaultdict(list)
for _ in range(m):
    u, v, c, w = map(int, sys.stdin.readline().split())
    edges.append((u, v, c, w))
    graph[u].append(len(edges) - 1)
    edges.append((v, u, 0, -w))
    graph[v].append(len(edges) - 2)

# Max Flow Min Cost using Edmonds-Karp and Dijkstra's algorithm
def max_flow_min_cost():
    INF = float('inf')
    n = len(graph)
    source, sink = s, t
    max_flow = 0
    min_cost = 0
    
    while True:
        # Run BFS to find augmenting path
        queue = deque([source])
        prev_node = [-1] * n
        min_capacity = [0] * n
        min_capacity[source] = INF
        
        while queue and prev_node[sink] == -1:
            u = queue.popleft()
            for idx in graph[u]:
                edge = edges[idx]
                v, c, w = edge[1], edge[2], edge[3]
                if prev_node[v] == -1 and c > 0:
                    prev_node[v] = idx
                    min_capacity[v] = min(min_capacity[u], c)
                    queue.append(v)
        
        if prev_node[sink] == -1:
            break
        
        # Augment the path found
        path_flow = min_capacity[sink]
        max_flow += path_flow
        min_cost += path_flow * edges[prev_node[sink]][3]
        v = sink
        
        while v != source:
            idx = prev_node[v]
            edges[idx][2] -= path_flow
            edges[idx ^ 1][2] += path_flow
            v = edges[idx][0]
    
    return max_flow, min_cost

# Output the result
F, cost = max_flow_min_cost()
print(F, cost)