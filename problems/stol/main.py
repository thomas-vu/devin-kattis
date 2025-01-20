def count_people(R, C, apartment):
    # Create a 2D array to store the number of free squares around each cell
    free_squares = [[0] * C for _ in range(R)]
    
    # Calculate the number of free squares around each cell
    for i in range(R):
        for j in range(C):
            if apartment[i][j] == '.':
                if i == 0 or j == 0:
                    free_squares[i][j] = 1
                else:
                    free_squares[i][j] = (free_squares[i-1][j] + free_squares[i][j-1] -
                                          free_squares[i-1][j-1]) + 1
    
    # Calculate the maximum perimeter of a table that can be placed at each free square
    max_perimeter = 0
    for i in range(R):
        for j in range(C):
            if apartment[i][j] == '.':
                min_free = float('inf')
                for x in range(i, R):
                    for y in range(j, C):
                        if apartment[x][y] == '.':
                            perimeter = 2 * (x - i + 1) + 2 * (y - j + 1)
                            min_free = min(min_free, free_squares[x][y])
                            max_perimeter = max(max_perimeter, perimeter)
    
    return max_perimeter

# Read input
R, C = map(int, input().split())
apartment = [input() for _ in range(R)]

# Calculate the number of people Mirko can invite
result = count_people(R, C, apartment)
print(result)