def find_mills(board):
    mills = []
    
    # Check horizontal mills
    for i in range(7):
        if board[i][0] == 'W' and board[i][2] == 'W' and board[i][4] == 'W':
            mills.append(((i, 0), (i, 2), (i, 4)))
        if board[i][2] == 'W' and board[i][4] == 'W' and board[i][6] == 'W':
            mills.append(((i, 2), (i, 4), (i, 6)))
        if board[i][0] == 'B' and board[i][2] == 'B' and board[i][4] == 'B':
            mills.append(((i, 0), (i, 2), (i, 4)))
        if board[i][2] == 'B' and board[i][4] == 'B' and board[i][6] == 'B':
            mills.append(((i, 2), (i, 4), (i, 6)))
    
    # Check vertical mills
    for j in range(7):
        if board[0][j] == 'W' and board[2][j] == 'W' and board[4][j] == 'W':
            mills.append(((0, j), (2, j), (4, j)))
        if board[2][j] == 'W' and board[4][j] == 'W' and board[6][j] == 'W':
            mills.append(((2, j), (4, j), (6, j)))
        if board[0][j] == 'B' and board[2][j] == 'B' and board[4][j] == 'B':
            mills.append(((0, j), (2, j), (4, j)))
        if board[2][j] == 'B' and board[4][j] == 'B' and board[6][j] == 'B':
            mills.append(((2, j), (4, j), (6, j)))
    
    return mills

def is_double_mill(board):
    mills = find_mills(board)
    white_pieces = [(i, j) for i in range(7) for j in range(7) if board[i][j] == 'W']
    black_pieces = [(i, j) for i in range(7) for j in range(7) if board[i][j] == 'B']
    
    for mill in mills:
        if len(white_pieces) >= 3 and all(piece in white_pieces for piece in mill):
            remaining_white = [piece for piece in white_pieces if piece not in mill]
            if len(remaining_white) == 1 and any(board[x][y] == 'B' for x, y in remaining_white):
                return True
        if len(black_pieces) >= 3 and all(piece in black_pieces for piece in mill):
            remaining_black = [piece for piece in black_pieces if piece not in mill]
            if len(remaining_black) == 1 and any(board[x][y] == 'W' for x, y in remaining_black):
                return True
    return False

# Read input
board = [input().strip() for _ in range(7)]

# Check for double mill and output result
if is_double_mill(board):
    print("double mill")
else:
    print("no double mill!")