from sys import stdin, stdout

def dfs(cave, parent, time_left):
    global visited, graph, max_visits
    if time_left < 0:
        return
    
    max_visits = max(max_visits, len(visited))
    
    for next_cave in graph[cave]:
        if next_cave not in visited:
            visited.add(next_cave)
            dfs(next_cave, cave, time_left - graph[cave][next_cave])
            visited.remove(next_cave)

# Read input
m, n = map(int, stdin.readline().split())
graph = {i: {} for i in range(m)}
for _ in range(m - 1):
    u, v, t = map(int, stdin.readline().split())
    graph[u][v] = t
    graph[v][u] = t

# Initialize variables
visited = set([0])
max_visits = 0

# Perform DFS to find the maximum number of caves Sven can visit
dfs(0, -1, n)

# Output the result
stdout.write(str(max_visits - 1) + '\n')