def min_max_mud_depth(grid):
    r, c = len(grid), len(grid[0])
    
    # Helper function to perform DFS from a given cell
    def dfs(x, y):
        if x < 0 or x >= r or y < 0 or y >= c:
            return float('inf')
        if y == c - 1:
            return grid[x][y]
        visited[x][y] = True
        min_depth = float('inf')
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                min_depth = min(min_depth, dfs(nx, ny))
        visited[x][y] = False
        return min_depth if min_depth != float('inf') else grid[x][y]
    
    # Initialize visited array and find minimum max depth
    visited = [[False for _ in range(c)] for _ in range(r)]
    min_max_depth = float('inf')
    
    for i in range(r):
        min_max_depth = min(min_max_depth, dfs(i, 0))
    
    return min_max_depth

# Read input
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

# Output the result
print(min_max_mud_depth(grid))