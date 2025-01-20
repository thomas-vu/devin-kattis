def find_mines(grid):
    mines = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '*':
                mines.append((i + 1, j + 1))
    return mines

# Read input
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Find mines and print the result
mines = find_mines(grid)
print(len(mines))
for mine in mines:
    print(mine[0], mine[1])