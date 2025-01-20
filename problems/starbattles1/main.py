def is_valid(puzzle, solution):
    regions = {}
    for i in range(10):
        for j in range(10):
            region = puzzle[i][j]
            if region not in regions:
                regions[region] = set()
            regions[region].add((i, j))
    
    def count_stars(grid):
        return sum(row.count('*') for row in grid)
    
    def check_adjacent(x, y):
        if x > 0 and grid[x-1][y] == '*': return True
        if x < 9 and grid[x+1][y] == '*': return True
        if y > 0 and grid[x][y-1] == '*': return True
        if y < 9 and grid[x][y+1] == '*': return True
        return False
    
    def check_row(grid):
        for row in grid:
            if row.count('*') != 2: return False
        return True
    
    def check_col(grid):
        for col in zip(*grid):
            if list(col).count('*') != 2: return False
        return True
    
    def check_region(grid, region):
        for x, y in regions[region]:
            if grid[x][y] == '*':
                if check_adjacent(x, y): return False
        return True
    
    grid = [list(solution[i*10:(i+1)*10]) for i in range(10)]
    
    if not check_row(grid) or not check_col(grid): return "invalid"
    
    for region in regions:
        if not check_region(grid, region): return "invalid"
    
    return "valid"

# Read input
puzzle = [input().strip() for _ in range(10)]
solution = ''.join([input().strip() for _ in range(10)])

# Check solution
result = is_valid(puzzle, solution)
print(result)