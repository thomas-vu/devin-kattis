def min_moves(seats):
    n = len(seats)
    min_moves = float('inf')
    
    for i in range(n):
        if seats[i] == 'E':
            continue
        moves = 0
        for j in range(n):
            if seats[j] == 'B':
                moves += abs(i - j)
        min_moves = min(min_moves, moves)
    
    return min_moves

# Read input from stdin
seats = input().strip()
print(min_moves(seats))