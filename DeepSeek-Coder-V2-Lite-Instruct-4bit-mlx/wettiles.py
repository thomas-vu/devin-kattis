def simulate_rain(x, y, leaks, walls, t):
    # Initialize the grid with zeros
    grid = [[0 for _ in range(y)] for _ in range(x)]
    
    # Mark the leak locations with ones
    for leak in leaks:
        grid[leak[0] - 1][leak[1] - 1] = 1
    
    # Helper function to spread the water
    def spread_water(grid, x, y):
        new_grid = [[0 for _ in range(y)] for _ in range(x)]
        for i in range(x):
            for j in range(y):
                if grid[i][j] == 1:
                    # Spread to adjacent tiles
                    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < x and 0 <= nj < y:
                            new_grid[ni][nj] = 1
        return new_grid
    
    # Simulate the rain for t minutes
    for _ in range(t):
        grid = spread_water(grid, x, y)
    
    # Count the number of wet tiles
    count = 0
    for row in grid:
        for tile in row:
            if tile == 1:
                count += 1
    return count

# Read input and process each house
while True:
    line = list(map(int, input().split()))
    if line[0] == -1:
        break
    x, y, t, l, w = line
    leaks = []
    for _ in range(l):
        leak_pos = list(map(int, input().split()))
        leaks.append((leak_pos[0], leak_pos[1]))
    walls = []
    for _ in range(w):
        wall_pos = list(map(int, input().split()))
        walls.append(((wall_pos[0], wall_pos[1]), (wall_pos[2], wall_pos[3])))
    
    # Simulate and output the result for each house
    result = simulate_rain(x, y, leaks, walls, t)
    print(result)