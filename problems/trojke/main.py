def count_triplets(grid):
    N = len(grid)
    triplets = 0
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] != '.':
                # Check horizontally
                if j + 2 < N and grid[i][j + 1] != '.' and grid[i][j + 2] != '.':
                    if grid[i][j] == grid[i][j + 1] and grid[i][j] == grid[i][j + 2]:
                        triplets += 1
                # Check vertically
                if i + 2 < N and grid[i + 1][j] != '.' and grid[i + 2][j] != '.':
                    if grid[i][j] == grid[i + 1][j] and grid[i][j] == grid[i + 2][j]:
                        triplets += 1
                # Check diagonally (both directions)
                if i + 2 < N and j + 2 < N:
                    if grid[i + 1][j + 1] != '.' and grid[i + 2][j + 2] != '.':
                        if grid[i][j] == grid[i + 1][j + 1] and grid[i][j] == grid[i + 2][j + 2]:
                            triplets += 1
                    if i - 2 >= 0 and j + 2 < N:
                        if grid[i - 1][j + 1] != '.' and grid[i - 2][j + 2] != '.':
                            if grid[i][j] == grid[i - 1][j + 1] and grid[i][j] == grid[i - 2][j + 2]:
                                triplets += 1
    return triplets

# Read input
N = int(input())
grid = [input().strip() for _ in range(N)]

# Count and output the number of triplets
print(count_triplets(grid))