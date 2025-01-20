def is_correct(grid):
    n = len(grid)
    
    # Check rows and columns for equal number of black and white squares
    for i in range(n):
        black_count = grid[i].count('B')
        white_count = n - black_count
        if black_count != white_count:
            return False
    
    for j in range(n):
        black_count = sum(grid[i][j] == 'B' for i in range(n))
        white_count = n - black_count
        if black_count != white_count:
            return False
    
    # Check for consecutive same color squares in rows and columns
    for i in range(n):
        for j in range(n - 2):
            if all(grid[i][j + k] == grid[i][j] for k in range(3)):
                return False
    
    for j in range(n):
        for i in range(n - 2):
            if all(grid[i + k][j] == grid[i][j] for k in range(3)):
                return False
    
    return True

n = int(input())
grid = [input() for _ in range(n)]
print(1 if is_correct(grid) else 0)