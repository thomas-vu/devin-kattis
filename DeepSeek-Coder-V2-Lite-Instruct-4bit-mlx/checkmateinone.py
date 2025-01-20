def can_checkmate(board):
    # Find the positions of Yraglac's king and rook, and the opponent's king
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'K':
                king_pos = (i, j)
            elif board[i][j] == 'R':
                rook_pos = (i, j)
            elif board[i][j] == 'k':
                opponent_king_pos = (i, j)
    
    # Check if the rook can move to a position where it threatens the opponent's king
    for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = rook_pos[0] + direction[0], rook_pos[1] + direction[1]
        if 0 <= ni < 8 and 0 <= nj < 8:
            if board[ni][nj] == 'k':
                return "Yes"
    return "No"

# Read the board from input
board = [input().strip() for _ in range(8)]
print(can_checkmate(board))