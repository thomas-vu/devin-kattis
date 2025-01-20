import sys
from collections import defaultdict

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(m):
    a, b, x, y, z = map(int, sys.stdin.readline().split())
    edges[a].append((b, x, y, z))
    edges[b].append((a, -x, -y, -z))  # Add reverse edge with opposite translation

# Function to check if the diagram is commutative
def is_commutative(edges, n):
    visited = [False] * (n + 1)
    
    def dfs(node, path_translations):
        if visited[node]:
            return False
        visited[node] = True
        for neighbor, x, y, z in edges[node]:
            if (x, y, z) not in path_translations:
                new_path_translations = path_translations.copy()
                new_path_translations[(x, y, z)] = True
                if not dfs(neighbor, new_path_translations):
                    return False
        visited[node] = False  # Backtrack
        return True
    
    for i in range(1, n + 1):
        if not dfs(i, {}):
            return "Neibb"
    return "Jebb"

# Check and print the result
result = is_commutative(edges, n)
print(result)