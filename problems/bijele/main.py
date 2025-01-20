def calculate_needed_pieces(kings, queens, rooks, bishops, knights, pawns):
    required = {
        'kings': 1,
        'queens': 2,
        'rooks': 2,
        'bishops': 2,
        'knights': 2,
        'pawns': 8
    }
    
    to_add = {}
    for piece, count in required.items():
        needed = count - eval(piece)
        to_add[piece] = needed
    
    return [to_add['kings'], to_add['queens'], to_add['rooks'], to_add['bishops'], to_add['knights'], to_add['pawns']]

# Read input from stdin
inputs = list(map(int, input().split()))
kings, queens, rooks, bishops, knights, pawns = inputs

# Calculate the needed pieces
needed_pieces = calculate_needed_pieces(kings, queens, rooks, bishops, knights, pawns)

# Output the result
print(' '.join(map(str, needed_pieces)))