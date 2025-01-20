def count_simple_loops(m, connections):
    graph = {i: [] for i in range(m)}
    for s, t in connections:
        graph[s].append(t)
    
    def dfs(node, path):
        if node in path:
            return len(path) == 1 + (0 in path)
        visited.add(node)
        path.add(node)
        count = 0
        for neighbor in graph[node]:
            if len(path) > 1 and neighbor == path[-2]:
                continue
            count += dfs(neighbor, path)
        visited.remove(node)
        path.remove(node)
        return count
    
    unique_loops = set()
    for i in range(m):
        visited = set()
        dfs(i, set([i]))
    return len(unique_loops)

# Read input
m = int(input())
n = int(input())
connections = [tuple(map(int, input().split())) for _ in range(n)]

# Output the number of unique simple loops
print(count_simple_loops(m, connections))