import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(treehouses, edges):
    n = len(treehouses)
    parent = list(range(n))
    rank = [0] * n
    result_edges = []
    total_weight = 0.0

    for edge in edges:
        u, v = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            result_edges.append((u, v))
            total_weight += distance(treehouses[u][0], treehouses[u][1], treehouses[v][0], treehouses[v][1])

    return total_weight, result_edges

# Read input
n, e, p = map(int, input().split())
treehouses = [list(map(float, input().split())) for _ in range(n)]
edges = []
for _ in range(p):
    a, b = map(int, input().split())
    edges.append((a - 1, b - 1))

# Build graph and find MST with added edges
all_edges = []
for i in range(n):
    for j in range(i + 1, n):
        all_edges.append((i, j, distance(treehouses[i][0], treehouses[i][1], treehouses[j][0], treehouses[j][1])))

# Sort edges by weight
all_edges.sort(key=lambda x: x[2])

# Find minimum spanning tree (MST) using Kruskal's algorithm
mst_weight, mst_edges = kruskal_mst(treehouses, edges)

# Output the minimum total length of new cable needed
print("{:.6f}".format(mst_weight))