def is_solvable(grid):
    def dfs(x, y, color):
        if (x, y) in visited:
            return False
        visited.add((x, y))
        if grid[x][y] == color:
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 4 and 0 <= ny < 4:
                    dfs(nx, ny, color)
            return True
        return False

    visited = set()
    colors = {}
    for i in range(4):
        for j in range(4):
            if grid[i][j] != 'W':
                color = grid[i][j]
                if color not in colors:
                    colors[color] = set()
                colors[color].add((i, j))
    
    if len(colors) == 3:
        colors['Y'] = set()
    
    for color, points in colors.items():
        if len(points) == 0:
            continue
        for x, y in points:
            if (x, y) not in visited:
                if not dfs(x, y, color):
                    return "not solvable"
    return "solvable"

grid = [input().strip() for _ in range(4)]
print(is_solvable(grid))