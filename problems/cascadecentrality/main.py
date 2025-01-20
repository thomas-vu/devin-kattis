def cascade_centrality(N, edges):
    from math import prod
    tree = [[] for _ in range(N + 1)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    def dfs(node, parent):
        paths = []
        for child in tree[node]:
            if child != parent:
                paths.extend(dfs(child, node))
        return [node] + (paths[0] if paths else [])
    
    cascade_centrality_values = []
    for i in range(1, N + 1):
        paths_i = [dfs(i, -1)]
        chi_P = 1
        for path in paths_i:
            degree_product = prod([len(tree[node]) for node in path])
            chi_P *= degree_product
        cascade_centrality = 1 + sum(chi_P for path in paths_i)
        cascade_centrality_values.append(cascade_centrality / (N - 1))
    
    return sum(cascade_centrality_values) / N

# Read input
N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

# Calculate and print the mean of cascade centralities
mean_cascade_centrality = cascade_centrality(N, edges)
print("{:.6f}".format(mean_cascade_centrality))