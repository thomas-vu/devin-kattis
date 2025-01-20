from collections import defaultdict, deque

def bfs(start, n, graph, capacity):
    parent = [-1] * (n + 1)
    queue = deque()
    queue.append(start)
    visited = [False] * (n + 1)
    visited[start] = True
    
    while queue:
        u = queue.popleft()
        
        for v in graph[u]:
            if not visited[v] and capacity[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                if v == n:
                    return True, parent
    
    return False, parent

def edmonds_karp(n, m, f, c, v, edges):
    graph = defaultdict(list)
    capacity = [[0] * (n + 1) for _ in range(n + 1)]
    
    for u, v, x in edges:
        graph[u].append(v)
        graph[v].append(u)
        capacity[u][v] += x
        capacity[v][u] += x
    
    source = f
    sink = v
    max_flow = 0
    
    while True:
        found, parent = bfs(source, n, graph, capacity)
        if not found:
            break
        
        path_flow = float('Inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s])
            s = parent[s]
        
        max_flow += path_flow
        
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u
    
    return max_flow

# Read input
n, m = map(int, input().split())
f, c, v = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

# Calculate and print the result
result = edmonds_karp(n, m, f, c, v, edges)
print(result)