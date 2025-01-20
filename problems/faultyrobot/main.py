n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
forced_moves = {}

for _ in range(m):
    a, b = map(int, input().split())
    if a > 0:
        edges[a].append(b)
    else:
        forced_moves[-a] = b

def dfs(node, visited):
    if node in visited:
        return []
    visited.add(node)
    path = [node]
    for neighbor in edges[node]:
        path += dfs(neighbor, visited)
    return path

possible_stops = set()
visited = set()
buggy_move = False
for node in range(1, n + 1):
    if node not in visited:
        path = dfs(node, visited)
        for stop_node in path:
            if stop_node in forced_moves and not buggy_move:
                next_node = forced_moves[stop_node]
                path = dfs(next_node, visited)
                for stop in path:
                    possible_stops.add(stop)
                buggy_move = True
            else:
                possible_stops.add(stop_node)
        visited |= set(path)
    else:
        if node in forced_moves and not buggy_move:
            next_node = forced_moves[node]
            path = dfs(next_node, visited)
            for stop in path:
                possible_stops.add(stop)
            buggy_move = True
        else:
            possible_stops.add(node)

print(len(possible_stops))