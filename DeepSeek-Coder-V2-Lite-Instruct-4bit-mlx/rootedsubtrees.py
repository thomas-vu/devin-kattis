import sys
sys.setrecursionlimit(200000)
from collections import defaultdict, deque

# Read input
n, q = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]
queries = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]

# Build the tree
tree = defaultdict(list)
for u, v in edges:
    tree[u].append(v)
    tree[v].append(u)

# DFS to find the subtree size for each node
subtree_size = [0] * (n + 1)
def dfs(node, parent):
    size = 1
    for child in tree[node]:
        if child != parent:
            size += dfs(child, node)
    subtree_size[node] = size
    return size
dfs(1, -1)

# Process each query
results = []
for r, p in queries:
    # Use DFS to find the nodes in the subtree of each root for both roots
    def dfs_subtree(root, x):
        visited = set()
        stack = [x]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                for child in tree[node]:
                    if child not in visited:
                        stack.append(child)
        return visited
    
    subtree_r = dfs_subtree(r, r)
    subtree_p = dfs_subtree(p, p)
    
    # Find the intersection of the subtrees and count distinct sets
    obtainable_sets = subtree_r & subtree_p
    result = len(obtainable_sets) if obtainable_sets else 0
    results.append(result)

# Output the results
for result in results:
    print(result)