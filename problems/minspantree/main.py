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

def kruskal(n, edges):
    edges = sorted(edges)
    parent = [i for i in range(n)]
    rank = [0] * n
    result = []
    total_cost = 0

    for edge in edges:
        u, v, w = edge
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append((u, v))
            union(parent, rank, x, y)
            total_cost += w

    if len(result) == n - 1:
        return total_cost, result
    else:
        return "Impossible", []

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))

    cost, mst = kruskal(n, edges)
    if cost == "Impossible":
        print("Impossible")
    else:
        print(cost)
        for edge in sorted(mst, key=lambda x: (x[0], x[1])):
            print(edge[0], edge[1])