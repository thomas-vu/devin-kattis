def min_moves_to_rectangle(N, M, cubes):
    # Convert the list of cube positions to a set of coordinates for easy access
    cube_positions = {(r, c) for r, c in cubes}
    
    # Find the minimum and maximum row and column indices of the cubes
    min_row = min(cubes, key=lambda x: x[0])[0]
    max_row = max(cubes, key=lambda x: x[0])[0]
    min_col = min(cubes, key=lambda x: x[1])[1]
    max_col = max(cubes, key=lambda x: x[1])[1]
    
    # Calculate the number of moves required to arrange cubes into a rectangle
    moves = 0
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if (r, c) not in cube_positions:
                moves += 1
    
    return moves

# Read input from stdin
N, M = map(int, input().split())
cubes = [tuple(map(int, input().split())) for _ in range(M)]

# Output the result
print(min_moves_to_rectangle(N, M, cubes))