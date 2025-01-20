def can_fold(grid):
    # Helper function to count the number of unit squares in the connected component
    def count_squares(x, y):
        if x < 0 or x >= 6 or y < 0 or y >= 6 or grid[x][y] == '.':
            return 0
        count = 1
        grid[x][y] = '.'
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            count += count_squares(x + dx, y + dy)
        return count

    # Check if the grid is valid and connected
    for i in range(6):
        for j in range(6):
            if grid[i][j] == '#':
                # Count the number of squares in the connected component
                if count_squares(i, j) != 6:
                    return "cannot fold"
                # Ensure no 2x2 square of unit squares exists
                if i <= 4 and j <= 4:
                    if grid[i+1][j] == '#' and grid[i][j+1] == '#' and grid[i+1][j+1] == '#':
                        return "cannot fold"
                break
    # Check if the connected component can form a unit cube
    for i in range(6):
        for j in range(6):
            if grid[i][j] == '#':
                # Check the shape of the connected component to determine if it can fold into a cube
                sides = 0
                for x in range(6):
                    for y in range(6):
                        if grid[x][y] == '#':
                            if x == 0 or x == 5 or y == 0 or y == 5:
                                sides += 1
                if sides != 8:
                    return "cannot fold"
                else:
                    return "can fold"
    return "cannot fold"

# Read the input grid
grid = [list(input().strip()) for _ in range(6)]
# Output the result
print(can_fold(grid))