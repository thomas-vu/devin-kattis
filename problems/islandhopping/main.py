import math
from itertools import combinations

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def kruskal_mst(points):
    edges = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            edges.append((distance(points[i], points[j]), i, j))
    edges.sort()
    
    parent = list(range(len(points)))
    rank = [0] * len(points)
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            else:
                parent[root_u] = root_v
                if rank[root_u] == rank[root_v]:
                    rank[root_v] += 1
    
    mst_weight = 0
    for edge in edges:
        weight, u, v = edge
        if find(u) != find(v):
            union(u, v)
            mst_weight += weight
    return mst_weight

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(cases):
        num_islands = int(data[index])
        index += 1
        islands = []
        for _ in range(num_islands):
            x = float(data[index])
            y = float(data[index + 1])
            islands.append((x, y))
            index += 2
        mst_weight = kruskal_mst(islands)
        results.append("{:.3f}".format(mst_weight))
    
    print("\n".join(results))

if __name__ == "__main__":
    main()