def can_form_skylines(R, C, east_skies, north_skies):
    # Create a 2D array to store the building heights
    grid = [[0] * C for _ in range(R)]
    
    # Fill the grid based on the eastern and northern skylines
    for i in range(R):
        for j in range(C):
            # The height of the building at (i, j) is determined by the minimum of the
            # tallest buildings in its row and column minus one to account for zero-based indexing
            grid[i][j] = min(east_skies[i], north_skies[j]) - 1
    
    # Check if the resulting skylines match the given ones
    for i in range(R):
        if max(grid[i]) != east_skies[i]:
            return "impossible"
    
    for j in range(C):
        if max([grid[i][j] for i in range(R)]) != north_skies[j]:
            return "impossible"
    
    return "possible"

# Read input
R, C = map(int, input().split())
east_skies = list(map(int, input().split()))
north_skies = list(map(int, input().split()))

# Output the result
print(can_form_skylines(R, C, east_skies, north_skies))