import sys
from math import inf

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

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

def kruskal_mst(points):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            edges.append((dist, i, j))
    edges.sort()

    parent = [i for i in range(n)]
    rank = [0] * n
    result_edges = []
    total_weight = 0

    for edge in edges:
        weight, u, v = edge
        if find(parent, u) != find(parent, v):
            union(parent, rank, u, v)
            result_edges.append((u, v))
            total_weight += weight
    return total_weight

# Read input
input_lines = sys.stdin.read().strip().split('\n')
N = int(input_lines[0])
points = [tuple(map(int, line.split())) for line in input_lines[1:]]

# Calculate and print the result
result = kruskal_mst(points)
print(result)