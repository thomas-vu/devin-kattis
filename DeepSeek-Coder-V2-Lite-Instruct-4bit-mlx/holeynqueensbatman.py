def is_safe(board, row, col):
    n = len(board)
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 'Q':
            return False
    return True

def solve_nqueens(board, row):
    n = len(board)
    if row == n:
        return 1
    solutions = 0
    for col in range(n):
        if board[row][col] != '#' and is_safe(board, row, col):
            board[row][col] = 'Q'
            solutions += solve_nqueens(board, row + 1)
            board[row][col] = '.'
    return solutions

def count_solutions(N, holes):
    board = [['.' for _ in range(N)] for _ in range(N)]
    for row, col in holes:
        board[row][col] = '#'
    return solve_nqueens(board, 0)

while True:
    line = input().split()
    N = int(line[0])
    M = int(line[1])
    if N == 0 and M == 0:
        break
    holes = []
    for _ in range(M):
        row, col = map(int, input().split())
        holes.append((row, col))
    print(count_solutions(N, holes))