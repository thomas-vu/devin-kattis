def count_coast(grid, N, M):
    def dfs(x, y):
        if (x, y) in visited:
            return 0
        visited.add((x, y))
        if grid[x][y] == 0:
            return 0
        coast = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 0:
                    coast += 1
                elif (nx, ny) not in visited:
                    coast += dfs(nx, ny)
        return coast
    
    visited = set()
    coast_length = 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                coast_length += dfs(i, j)
    return coast_length

# Read input
N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# Process and output the result
result = count_coast([list(map(int, row)) for row in grid], N, M)
print(result)