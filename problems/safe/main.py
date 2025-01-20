def count_button_pushes(initial):
    # Convert the input to a 3x3 matrix
    grid = [list(map(int, initial[i:i+3])) for i in range(0, 9, 3)]
    
    # Function to increment the button and its neighbors
    def increment_button(x, y):
        if 0 <= x < 3 and 0 <= y < 3:
            grid[x][y] = (grid[x][y] + 1) % 4
            if x > 0: grid[x-1][y] = (grid[x-1][y] + 1) % 4
            if x < 2: grid[x+1][y] = (grid[x+1][y] + 1) % 4
            if y > 0: grid[x][y-1] = (grid[x][y-1] + 1) % 4
            if y < 2: grid[x][y+1] = (grid[x][y+1] + 1) % 4
    
    # Start from the top-left button and incrementally push buttons to reach all zeros
    pushes = 0
    for i in range(3):
        for j in range(3):
            while grid[i][j] != 0:
                increment_button(i, j)
                pushes += 1
    
    # Check if all buttons are zero
    for row in grid:
        if any(row):
            return -1
    
    return pushes

# Read input
inputs = [input().split() for _ in range(3)]
result = count_button_pushes(inputs)
print(result)