import math
from itertools import combinations

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def intersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)
    if d > r1 + r2 or d < abs(r1 - r2):
        return False
    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(r1 ** 2 - a ** 2)
    x0 = x1 + a * (x2 - x1) / d
    y0 = y1 + a * (y2 - y1) / d
    ix1 = x0 + h * (y2 - y1) / d
    iy1 = y0 - h * (x2 - x1) / d
    ix2 = x0 - h * (y2 - y1) / d
    iy2 = y0 + h * (x2 - x1) / d
    return ix1, iy1, ix2, iy2

def is_connected(edges):
    graph = {i: [] for i in range(len(dishes))}
    for (u, v) in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * len(dishes)
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    
    start_node = edges[0][0] if edges else 0
    dfs(start_node)
    return all(visited)

def min_beam_length(dishes):
    n = len(dishes)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if distance(dishes[i][0], dishes[i][1], dishes[j][0], dishes[j][1]) <= dishes[i][2] + dishes[j][2]:
                edges.append((i, j))
    
    min_length = float('inf')
    for subset in range(1, 1 << n):
        subset_edges = []
        for i in range(n):
            if subset & (1 << i):
                for j in range(i + 1, n):
                    if subset & (1 << j):
                        intersect_points = intersect(dishes[i][0], dishes[i][1], dishes[i][2], dishes[j][0], dishes[j][1], dishes[j][2])
                        if intersect_points:
                            subset_edges.append((i, j))
        if is_connected(subset_edges):
            total_length = sum(distance(*dishes[u], *dishes[v]) for u, v in subset_edges)
            min_length = min(min_length, total_length)
    
    return min_length if min_length != float('inf') else 0

# Read input
N = int(input())
dishes = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
result = min_beam_length(dishes)
print("{:.10f}".format(result))