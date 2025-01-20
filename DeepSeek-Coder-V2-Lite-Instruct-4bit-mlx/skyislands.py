def is_connected(N, bridges):
    if N == 1:
        return "YES"
    
    # Create adjacency list to represent the graph
    adj_list = {i: [] for i in range(1, N + 1)}
    for a, b in bridges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    # Use DFS to check if all islands are connected
    visited = [False] * (N + 1)
    
    def dfs(node):
        visited[node] = True
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    # Start DFS from the first island
    dfs(1)
    
    # Check if all islands are visited
    for i in range(1, N + 1):
        if not visited[i]:
            return "NO"
    
    return "YES"

# Read input
N, M = map(int, input().split())
bridges = [tuple(map(int, input().split())) for _ in range(M)]

# Output the result
print(is_connected(N, bridges))