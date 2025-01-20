def min_moves_to_rearrange_tanks(N, positions):
    moves = []
    row_positions = {i: (0, 0) for i in range(1, N + 1)}
    col_positions = {i: (0, 0) for i in range(1, N + 1)}
    
    # Initialize row and column positions
    for pos in positions:
        r, c = pos
        row_positions[r] = (r, c)
        col_positions[c] = (r, c)
    
    # Rearrange tanks to have each tank in a unique row and column
    for tank_num in range(1, N + 1):
        r, c = row_positions[tank_num]
        while r != tank_num:
            if r < tank_num:
                moves.append((tank_num, 'D'))
                r += 1
            else:
                moves.append((tank_num, 'U'))
                r -= 1
        
        while c != tank_num:
            if c < tank_num:
                moves.append((tank_num, 'R'))
                c += 1
            else:
                moves.append((tank_num, 'L'))
                c -= 1
    
    return moves

# Read input
N = int(input().strip())
positions = [tuple(map(int, input().strip().split())) for _ in range(N)]

# Get the minimum number of moves and the sequence of moves
moves = min_moves_to_rearrange_tanks(N, positions)

# Output the result
print(len(moves))
for move in moves:
    print(*move)