def spread_water(grid, N, M):
    # Create a copy of the grid to simulate the spread of water
    new_grid = [['.' for _ in range(M)] for _ in range(N)]
    
    # Helper function to spread water from a cell
    def spread_from(x, y):
        # Spread to the air directly above
        if x > 0 and grid[x-1][y] == 'V':
            new_grid[x][y] = 'V'
        # Spread to air cells directly left or right of a water cell
        if y > 0 and grid[x][y-1] == 'V':
            new_grid[x][y-1] = 'V'
        if y < M - 1 and grid[x][y+1] == 'V':
            new_grid[x][y+1] = 'V'
    
    # Initialize the new grid with the current state of water cells
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'V':
                spread_from(i, j)
    
    return new_grid

def main():
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]
    
    # Spread water until no more spread occurs
    while True:
        new_grid = spread_water(grid, N, M)
        if new_grid == grid:
            break
        grid = new_grid
    
    # Output the final state of the grid
    for row in grid:
        print(''.join(row))

if __name__ == "__main__":
    main()