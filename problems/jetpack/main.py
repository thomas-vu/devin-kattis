def solve(N, field):
    moves = []
    
    # Find the initial position of Mirko's jetpack
    start_col = 0
    while field[9][start_col] == 'X':
        start_col += 1
    
    # Simulate the game to find the moves
    t = 1
    while start_col < N:
        # Check if the next move is possible without hitting an obstacle
        next_col = start_col
        while next_col < N and field[9][next_col] == '.':
            next_col += 1
        
        # If no more moves are possible, end the game
        if next_col == start_col:
            break
        
        # Record the move
        moves.append((t, next_col - start_col))
        
        # Update the position for the next move
        start_col = next_col
        
        # Move up and right to the new position
        for row in range(9, -1, -1):
            if next_col < N and field[row][next_col] == '.':
                start_col = next_col
            else:
                break
        
        # Increment the time by 1 second for each move
        t += 1
    
    # Output the number of moves and the moves themselves
    print(len(moves))
    for move in moves:
        print(*move)

# Read input
N = int(input())
field = [input() for _ in range(10)]

# Solve the problem and output the solution
solve(N, field)