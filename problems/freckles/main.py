import math
from itertools import combinations

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def kruskal_mst(points):
    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
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
    
    mst_cost = 0
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_cost += cost
    return mst_cost

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    while index < len(data):
        n = int(data[index])
        if n == 0:
            break
        points = []
        for i in range(n):
            x = float(data[index + 1 + i * 2])
            y = float(data[index + 2 + i * 2])
            points.append((x, y))
        index += 2 + n * 2
        
        mst_cost = kruskal_mst(points)
        print("{:.2f}".format(mst_cost))
        if index < len(data):
            print()

if __name__ == "__main__":
    main()