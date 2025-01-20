# This code is designed to solve the given problem using a flood fill algorithm (DFS or BFS)
# to determine landlockedness for each country on the map.

def dfs(x, y, visited, graph, borders):
    stack = [(x, y)]
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]: continue
        visited[cx][cy] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                if graph[nx][ny] == 'W':
                    borders[country_map[cx][cy]] = min(borders.get(country_map[cx][cy], float('inf')), step)
                elif not visited[nx][ny]:
                    stack.append((nx, ny))

N, M = map(int, input().split())
graph = [input() for _ in range(N)]
country_map = [[None] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
borders = {}
countries = set()

# Assign each country a unique identifier and find the borders between countries.
for i in range(N):
    for j in range(M):
        if graph[i][j] != 'W':
            country = graph[i][j]
            if country not in countries:
                countries.add(country)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < M:
                    if graph[ni][nj] == 'W':
                        country_map[i][j] = country
                        break
                else:
                    if graph[ni][nj] != 'W':
                        country_map[i][j] = graph[ni][nj]
            if country_map[i][j] is None:
                country_map[i][j] = graph[i][j]

# Calculate the landlockedness for each country using DFS.
for i in range(N):
    for j in range(M):
        if graph[i][j] != 'W' and not visited[i][j]:
            dfs(i, j, visited, graph, borders)

# Output the results.
for country in sorted(countries):
    print(country, borders[country] if country in borders else 0)