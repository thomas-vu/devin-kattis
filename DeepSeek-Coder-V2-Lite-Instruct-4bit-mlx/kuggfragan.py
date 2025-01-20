def can_gears_work(N, M, connections):
    graph = {i: set() for i in range(N)}
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)
    
    visited = [False] * N
    
    def dfs(node, parent):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, node):
                    return True
            elif neighbor != parent:
                return True
        return False
    
    for i in range(N):
        if not visited[i]:
            if dfs(i, -1):
                return "attend here"
    return "no way"

# Read input
N, M = map(int, input().split())
connections = [list(map(int, input().split())) for _ in range(M)]

# Output the result
print(can_gears_work(N, M, connections))