def can_divide_items(N, items, M, suspicious_pairs):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for pair in suspicious_pairs:
        u, v = pair
        graph[u].append(v)
        graph[v].append(u)
    
    colors = {}
    
    def dfs(node, color):
        if node in colors:
            return colors[node] == color
        colors[node] = color
        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - color):
                return False
        return True
    
    for item in items:
        if item not in colors:
            if not dfs(item, 0):
                return "impossible"
    
    walt_items = [item for item in items if colors[item] == 0]
    jesse_items = [item for item in items if colors[item] == 1]
    
    return "\n".join([", ".join(walt_items), ", ".join(jesse_items)])

# Read input
N = int(input())
items = [input().strip() for _ in range(N)]
M = int(input())
suspicious_pairs = [input().strip().split() for _ in range(M)]

# Output the result
result = can_divide_items(N, items, M, suspicious_pairs)
print(result)