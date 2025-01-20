def is_valid(board, row, col, num):
    for x in range(6):
        if board[row][x] == num or board[x][col] == num:
            return False
    for x in range(3):
        for y in range(3):
            if board[x + (row // 2) * 3][y + (col // 3) * 2] == num:
                return False
    return True

def solve(board):
    for i in range(6):
        for j in range(6):
            if board[i][j] == '-':
                for num in map(str, range(1, 10)):
                    if (board[i][j] == '/' and len(num) > 1):
                        continue
                    if (board[i][j] == '/' and len(num) == 1):
                        num = '0' + num
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = '-'
                return False
    return True

def parse_input(lines):
    board = [list(line.split()) for line in lines]
    return [[cell if len(cell) == 1 else cell.split('/') for cell in row] for row in board]

def print_board(board):
    for row in board:
        print(' '.join([str(cell) if len(cell) == 1 else '/'.join(cell) for cell in row]))

lines = [
    "-/- -/5 4 3 2 -/-",
    "- 6 -/- -/- - -/-",
    "- 7/- - -/- -/- 2",
    "8 -/- -/- - -/3 -",
    "-/- - -/- -/- 4 -",
    "-/- 8 7 6 5/- -/-7/9 1/5 4 3 2 6/8"
]

board = parse_input(lines)
solve(board)
print_board(board)