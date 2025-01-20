def simulate_gravity(R, C, grid):
    # Create a new grid to store the final state
    final_grid = [['.' for _ in range(C)] for _ in range(R)]
    
    # Iterate over each column to apply gravity
    for col in range(C):
        row_index = R - 1
        # Iterate over each cell in the column from bottom to top
        for row in range(R - 1, -1, -1):
            if grid[row][col] == 'a':
                # Place the apple in the final position after applying gravity
                final_grid[row_index][col] = 'a'
                row_index -= 1
            elif grid[row][col] == '#':
                # Obstacle remains in its position
                final_grid[row][col] = '#'
    
    # Print the final configuration of the board
    for row in final_grid:
        print(''.join(row))

# Read input
import sys
input = sys.stdin.read
data = input().split()
R, C = int(data[0]), int(data[1])
grid = data[2:]

# Simulate gravity and print the final configuration
simulate_gravity(R, C, grid)