def find_hives(n, paths):
    graph = {i: [] for i in range(n)}
    for u, v in paths:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    component_count = 0
    
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    for i in range(n):
        if not visited[i]:
            dfs(i)
            component_count += 1
    
    if component_count == 1:
        return n
    elif component_count > 2:
        return 'impossible'
    else:
        return min(component_count, n // 2)

# Read input
n, m = map(int, input().split())
paths = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(find_hives(n, paths))