def min_statues_to_move(grid):
    n, m = len(grid), len(grid[0])
    statues = []
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                statues.append(grid[i][j])
    
    statues.sort()
    
    min_moves = float('inf')
    
    for start in range(n + m - 1):
        moves = 0
        temp_statues = statues.copy()
        for diagonal in range(start, -1, -1):
            pos = start - diagonal
            if pos < 0 or pos >= n:
                continue
            for j in range(min(m, diagonal + 1)):
                if pos + j < n and start - diagonal + j < m:
                    if grid[pos + j][start - diagonal + j] == -1:
                        temp_statues.pop(0)
                    else:
                        moves += abs(grid[pos + j][start - diagonal + j] - temp_statues[0])
                        temp_statues.pop(0)
        min_moves = min(min_moves, moves)
    
    for start in range(1, m + n - 1):
        moves = 0
        temp_statues = statues.copy()
        for diagonal in range(start, n + m - 1):
            pos = diagonal - start
            if pos < 0 or pos >= m:
                continue
            for j in range(min(n, diagonal + 1)):
                if pos + j < m and diagonal - start + j < n:
                    if grid[diagonal - start + j][pos + j] == -1:
                        temp_statues.pop(0)
                    else:
                        moves += abs(grid[diagonal - start + j][pos + j] - temp_statues[0])
                        temp_statues.pop(0)
        min_moves = min(min_moves, moves)
    
    return min_moves

# Read input
n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

# Output the result
print(min_statues_to_move(grid))