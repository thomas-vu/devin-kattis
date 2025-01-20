def simulate_snowfall(grid, N, M):
    # Create a new grid to store the final configuration
    final_grid = [['.' for _ in range(M)] for _ in range(N)]
    
    # Iterate through each column and simulate the snowfall
    for j in range(M):
        # Find the height of the bottommost snow block in the current column
        bottom = N - 1
        while bottom >= 0 and grid[bottom][j] == 'S':
            bottom -= 1
        
        # Simulate the snowfall from this height downwards
        for i in range(bottom, -1, -1):
            if grid[i][j] == 'S':
                final_grid[bottom][j] = 'S'
                bottom -= 1
    
    return final_grid

# Read input
N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(input().strip()))

# Simulate the snowfall and get the final configuration
final_grid = simulate_snowfall(grid, N, M)

# Output the final configuration
for row in final_grid:
    print(''.join(row))