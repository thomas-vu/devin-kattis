def min_soldiers(grid, w, h):
    # Create a graph where each 'A' and 'B' is a node, and the edges represent adjacent positions
    graph = {i: [] for i in range(w * h) if grid[i] != '0'}
    edges = []
    
    for i in range(w * h):
        if grid[i] == 'A' or grid[i] == 'B':
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i // w + di, i % w + dj
                if 0 <= ni < h and 0 <= nj < w and grid[ni * w + nj] != '0':
                    edges.append((i, ni * w + nj))
    
    # Use Kruskal's algorithm to find the minimum spanning tree of the graph
    parent = list(range(len(graph)))
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        xroot = find(x)
        yroot = find(y)
        if xroot != yroot:
            parent[xroot] = yroot
    
    edges.sort(key=lambda x: int(grid[x[0]] if grid[x[0]] in 'AB' else 9))
    
    for edge in edges:
        u, v = edge
        if find(u) != find(v):
            union(u, v)
    
    # Count the number of soldiers needed to secure all nodes in the minimum spanning tree
    min_soldiers = 0
    for i in range(w * h):
        if grid[i] != '0' and find(i) == i:
            min_soldiers += int(grid[i]) if grid[i] not in 'AB' else 0
    
    return min_soldiers

# Read input
w, h = map(int, input().split())
grid = [input() for _ in range(h)]

# Output the result
print(min_soldiers(grid, w, h))