def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

def kruskal_mst(n, edges, insecure_buildings):
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    edges.sort(key=lambda x: x[2])
    
    mst_edges = []
    cost = 0
    
    for edge in edges:
        u, v, w = edge
        if find(parent, u) != find(parent, v) and (u not in insecure_buildings or v not in insecure_buildings):
            union(parent, rank, u, v)
            mst_edges.append((u, v))
            cost += w
    
    if len(mst_edges) == n - 1:
        return cost
    else:
        return "impossible"

# Read input
n, m, p = map(int, input().split())
insecure_buildings = set(map(int, input().split()))
edges = []
for _ in range(m):
    x_i, y_i, l_i = map(int, input().split())
    edges.append((x_i, y_i, l_i))

# Run Kruskal's algorithm to find the MST
result = kruskal_mst(n, edges, insecure_buildings)
print(result)