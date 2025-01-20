import sys
from math import inf
sys.setrecursionlimit(10**6)

def dfs(u, p):
    global k, max_resources
    size[u] = 1
    for v in graph[u]:
        if v != p:
            depth[v] = depth[u] + 1
            dfs(v, u)
            size[u] += size[v]
    if depth[u] > 0:
        edges.append((depth[u], u, size[u]))

def solve(node, parent, taken):
    global max_resources
    res = 0
    for child in graph[node]:
        if child != parent:
            res += solve(child, node, taken)
    if not edges or (edges and edges[-1][0] != depth[node]):
        edges.append((depth[node], node, 1))
    else:
        edges[-1] = (depth[node], node, min(edges[-1][2]+1, k))
        if edges[-1][2] <= k:
            res += edge_values[edges[-1][0]-1]
    if edges[-1][2] > k:
        taken = True
    else:
        taken = False
    if not taken:
        edges.pop()
    return res

N, k = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
edge_values = []
for _ in range(N-1):
    u, v, c = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    edge_values.append(c)

depth = [0] * (N+1)
size = [0] * (N+1)
edges = []
dfs(1, -1)
max_resources = 0
solve(1, -1, False)
print(max_resources)