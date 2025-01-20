def min_friends(V, E):
    graph = {i: [] for i in range(V)}
    for a, b in E:
        graph[a].append(b)
    
    def dfs(node, visited):
        if node == V - 1:
            return 1
        count = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                count += dfs(neighbor, visited)
        return count
    
    visited = set()
    visited.add(0)
    friends_needed = dfs(0, visited)
    
    return friends_needed

# Read input
V, E = map(int, input().split())
edges = []
for _ in range(E):
    a, b = map(int, input().split())
    edges.append((a, b))

# Output the result
print(min_friends(V, edges))