from collections import defaultdict
import sys

def read_ints():
    return list(map(int, input().split()))

def dfs(station, visited, graph, path_length):
    if len(visited) == n:
        return path_length + graph[station][0]
    min_path = float('inf')
    for next_station in graph[station]:
        if next_station not in visited:
            new_visited = visited.copy()
            new_visited.add(next_station)
            min_path = min(min_path, dfs(next_station, new_visited, graph, path_length + graph[station][next_station]))
    return min_path

while True:
    n, m = read_ints()
    if n == 0:
        break
    graph = defaultdict(dict)
    for _ in range(m):
        u, v, w = read_ints()
        graph[u][v] = w
        graph[v][u] = w
    min_path = float('inf')
    for start in range(1, n + 1):
        visited = set([start])
        min_path = min(min_path, dfs(start, visited, graph, 0))
    print(min_path)