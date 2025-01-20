# This code uses Tarjan's algorithm to find the strongly connected components in a directed graph.
# If there is more than one component, it's possible to throw bridges to connect them.
# Otherwise, it's not possible.

import sys
sys.setrecursionlimit(10**6)

def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = read_ints()
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

# Tarjan's algorithm to find strongly connected components
def dfs(v, graph, visited, stack, low):
    global time
    visited[v] = True
    stack.append(v)
    low[v] = time
    tin[v] = time
    time += 1
    
    for u in graph[v]:
        if not visited[u]:
            dfs(u, graph, visited, stack, low)
            low[v] = min(low[v], low[u])
        else:
            low[v] = min(low[v], tin[u])
    
    if low[v] == tin[v]:
        while stack:
            u = stack.pop()
            component.append(u)
            if u == v:
                break
        components.append(component[:-1])
        component.clear()

visited = [False] * N
tin = [-1] * N
low = [-1] * N
stack = []
components = []
component = []
time = 0

for i in range(N):
    if not visited[i]:
        dfs(i, graph, visited, stack, low)

if len(components) == 1:
    print("Nej")
else:
    print("Ja")
    K = len(components) - 1
    print(K)
    for i in range(1, K + 1):
        u = components[0][0]
        v = components[i][0]
        print(u + 1, v + 1, components[0][-1] + 1, components[i][-1] + 1)