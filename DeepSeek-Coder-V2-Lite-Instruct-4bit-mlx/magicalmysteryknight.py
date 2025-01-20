def is_valid(board, x, y):
    return 0 <= x < 8 and 0 <= y < 8 and board[x][y] == -1

def knight_moves(board, x, y):
    moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    possible_moves = []
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid(board, new_x, new_y):
            possible_moves.append((new_x, new_y))
    return possible_moves

def sum_row(board, row):
    return sum([board[row][col] for col in range(8)])

def sum_col(board, col):
    return sum([board[row][col] for row in range(8)])

def is_semi_magic(board):
    target_sum = 260
    for row in range(8):
        if sum_row(board, row) != target_sum:
            return False
    for col in range(8):
        if sum_col(board, col) != target_sum:
            return False
    return True

def fill_board(board):
    for row in range(8):
        for col in range(8):
            if board[row][col] == -1:
                for num in range(1, 65):
                    board[row][col] = num
                    if is_semi_magic(board):
                        break
                else:
                    board[row][col] = -1  # Reset if no valid number found
    return board

# Input processing
board = []
for _ in range(8):
    row = list(map(int, input().split()))
    board.append(row)

# Fill the missing labels to make it a semi-magical knight's tour
filled_board = fill_board(board)

# Output the result
for row in filled_board:
    print(" ".join(map(str, row)))