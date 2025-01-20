def place_coffee_shops(n, m, grid):
    # Create a copy of the grid to modify
    result_grid = [list(row) for row in grid]
    
    # Iterate over each cell in the grid
    for i in range(n):
        for j in range(m):
            # If the cell is land and not adjacent to another coffee shop
            if grid[i][j] == '.':
                # Check adjacent cells for coffee shops
                adj_water = False
                if i > 0 and grid[i-1][j] == 'E':
                    adj_water = True
                if i < n - 1 and grid[i+1][j] == 'E':
                    adj_water = True
                if j > 0 and grid[i][j-1] == 'E':
                    adj_water = True
                if j < m - 1 and grid[i][j+1] == 'E':
                    adj_water = True
                
                # If no adjacent coffee shop, place one
                if not adj_water:
                    result_grid[i][j] = 'E'
    
    # Convert the modified grid back to strings for output
    return [' '.join(row) for row in result_grid]

# Read input from stdin
n, m = map(int, input().split())
grid = [input() for _ in range(n)]

# Place coffee shops and output the result
result = place_coffee_shops(n, m, grid)
for line in result:
    print(line)