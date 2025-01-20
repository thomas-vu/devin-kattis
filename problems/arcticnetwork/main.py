import math

def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal_mst(edges, n):
    edges.sort()
    parent = [i for i in range(n)]
    rank = [0] * n
    mst_edges = []
    index = 0
    while len(mst_edges) < n - 1:
        u, v, w = edges[index]
        index += 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        if x != y:
            mst_edges.append((w, u, v))
            union(parent, rank, x, y)
    max_edge = 0
    for edge in mst_edges:
        if edge[0] > max_edge:
            max_edge = edge[0]
    return max_edge

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def main():
    n = int(input())
    for _ in range(n):
        s, p = map(int, input().split())
        outposts = [tuple(map(int, input().split())) for _ in range(p)]
        edges = []
        for i in range(p):
            for j in range(i + 1, p):
                dist = distance(*outposts[i], *outposts[j])
                edges.append((dist, i, j))
        min_distance = kruskal_mst(edges, p)
        print("{:.2f}".format(min_distance))

if __name__ == "__main__":
    main()