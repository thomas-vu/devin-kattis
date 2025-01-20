def can_place_knight(board, x, y):
    moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 'K':
            return False
    return True

def can_win(N):
    board = [['' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if can_place_knight(board, i, j):
                board[i][j] = 'K'
    
    if N == 1:
        return 'first'
    
    odd_count = sum(row.count('K') for row in board)
    
    if odd_count <= 1:
        return 'first'
    else:
        return 'second'

N = int(input().strip())
print(can_win(N))