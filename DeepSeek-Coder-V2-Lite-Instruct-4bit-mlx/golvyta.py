def min_grid_size(K, s, r, c):
    # Determine the minimum and maximum row and column positions reached by the robot
    min_row, max_row = r, r
    min_col, max_col = c, c
    
    # Process the instructions to find the bounds of the grid
    for instruction in s:
        if instruction == '>':
            min_col = max(min_col - 1, 0)
        elif instruction == 'v':
            min_row = max(min_row - 1, 0)
        elif instruction == '<':
            max_col = min(max_col + 1, c)
        elif instruction == '^':
            max_row = min(max_row + 1, r)
    
    # Calculate the possible dimensions of the grid based on the bounds found
    min_N = max_row - min_row + 1
    min_M = max_col - min_col + 1
    
    # Check if the calculated dimensions are consistent with the number of instructions
    moves = K - (max_row - min_row + 1) * (max_col - min_col + 1)
    if moves == 0 and min_N * min_M == K:
        return min_N * min_M
    else:
        return -1

# Read input
K = int(input())
s = input()
r, c = map(int, input().split())

# Calculate and print the result
print(min_grid_size(K, s, r, c))