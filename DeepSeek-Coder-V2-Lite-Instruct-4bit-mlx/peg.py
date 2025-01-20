def count_moves(board):
    moves = 0
    
    def is_valid(x, y):
        return 0 <= x < 7 and 0 <= y < 7
    
    def can_jump(x, y, dx, dy):
        nx, ny = x + 2 * dx, y + 2 * dy
        if is_valid(nx, ny) and board[x + dx][y + dy] == 'o' and board[nx][ny] == '.':
            return True
        return False
    
    for x in range(1, 5):
        for y in range(1, 5):
            if board[x][y] == 'o':
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if can_jump(x, y, dx, dy):
                        moves += 1
    return moves

# Read the board from input
board = [input().strip() for _ in range(7)]
print(count_moves(board))