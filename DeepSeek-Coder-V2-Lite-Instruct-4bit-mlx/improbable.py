def max_crates_stolen(r, c, grid):
    # Calculate the total number of crates initially
    total_crates = sum(sum(row) for row in grid)
    
    # Initialize the minimum possible height after heist
    min_height = float('inf')
    
    # Iterate over each possible configuration of the heist
    for i in range(r):
        for j in range(c):
            # Calculate the height of each pile after heist
            heights = [grid[x][y] for x in range(r) for y in range(c)]
            # Remove the pile at (i, j) and find the new minimum height
            heights.pop(i * c + j)
            min_height = min(min_height, sum(heights[k * c:(k + 1) * c]) / (r * c - 1))
    
    # Calculate the maximum number of crates that can be stolen
    max_stolen = int(min_height) * (r * c - 1)
    
    return max_stolen

# Read input
r, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(r)]

# Output the result
print(max_crates_stolen(r, c, grid))