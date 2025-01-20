def calculate_perimeter(R, K, house):
    # Convert the list of indices to a 3D grid representation
    grid = [[[0 for _ in range(R)] for _ in range(R)] for _ in range(R)]
    for index in house:
        x = (index - 1) // (R * R)
        y = (index - 1) // R % R
        z = (index - 1) % R
        grid[x][y][z] = 1
    
    # Calculate the perimeter
    perimeter = 0
    for x in range(R):
        for y in range(R):
            for z in range(R):
                if grid[x][y][z] == 1:
                    # Check all adjacent cells and count the sides that are not shared
                    if x == 0 or grid[x-1][y][z] == 0:
                        perimeter += 1
                    if x == R-1 or grid[x+1][y][z] == 0:
                        perimeter += 1
                    if y == 0 or grid[x][y-1][z] == 0:
                        perimeter += 1
                    if y == R-1 or grid[x][y+1][z] == 0:
                        perimeter += 1
                    if z == 0 or grid[x][y][z-1] == 0:
                        perimeter += 1
                    if z == R-1 or grid[x][y][z+1] == 0:
                        perimeter += 1
    return perimeter

# Read input
R, K = map(int, input().split())
house_indices = list(map(int, input().split()))

# Calculate and print the perimeter
perimeter = calculate_perimeter(R, K, house_indices)
print(perimeter)