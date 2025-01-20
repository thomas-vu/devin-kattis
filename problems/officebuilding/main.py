def max_tree_sum(r, c, land, s, t, floor_plan):
    def is_valid(x, y):
        return 0 <= x < r and 0 <= y < c and not visited[x][y]
    
    def dfs(x, y):
        if not is_valid(x, y) or land[x][y] == -1:
            return 0
        visited[x][y] = True
        size = land[x][y]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                size += dfs(nx, ny)
        return size
    
    def count_trees(x, y):
        total = 0
        for i in range(s):
            for j in range(t):
                if floor_plan[i][j] == '#' and is_valid(x + i, y + j):
                    total += land[x + i][y + j]
                elif floor_plan[i][j] == '.' and is_valid(x + i, y + j):
                    land[x + i][y + j] = -1
        return total
    
    visited = [[False for _ in range(c)] for _ in range(r)]
    max_sum = 0
    
    for i in range(r - s + 1):
        for j in range(c - t + 1):
            sum_trees = count_trees(i, j)
            max_sum = max(max_sum, sum_trees)
    
    return max_sum

# Read input
r, c = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(r)]
s, t = map(int, input().split())
floor_plan = [input() for _ in range(s)]

# Output the result
print(max_tree_sum(r, c, land, s, t, floor_plan))