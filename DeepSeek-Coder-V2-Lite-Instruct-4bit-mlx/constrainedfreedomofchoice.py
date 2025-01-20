def count_paths(grid, r, c):
    def dfs(x, y, visited):
        if x == r - 1 and y == c - 1:
            return 1
        paths = 0
        if x + 1 < r and grid[x + 1][y] == '.' and (x + 1, y) not in visited:
            paths += dfs(x + 1, y, visited | {(x, y)})
        if y + 1 < c and grid[x][y + 1] == '.' and (x, y + 1) not in visited:
            paths += dfs(x, y + 1, visited | {(x, y)})
        return paths
    
    return dfs(0, 0, set())

while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
    grid = [input() for _ in range(r)]
    print(count_paths(grid, r, c))