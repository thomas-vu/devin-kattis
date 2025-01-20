def check_winner(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '.':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '.':
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != '.':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '.':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if '.' in row:
            return False
    return True

def print_board(board):
    for row in board:
        print(''.join(row))

def make_move(board, move):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                new_board = [row[:] for row in board]
                new_board[i][j] = 'x' if move == 'first' else 'o'
                winner = check_winner(new_board)
                if winner:
                    return new_board, True
                if is_full(new_board):
                    return new_board, False
    for i in range(3):
        for j in range(3):
            if board[i][j] == '.':
                new_board = [row[:] for row in board]
                new_board[i][j] = 'o' if move == 'first' else 'x'
                winner = check_winner(new_board)
                if not winner:
                    return new_board, True
                if is_full(new_board):
                    return new_board, False
    return board, False

import sys

# Read the first move from stdin
move = input().strip()
board = [list(input().strip()) for _ in range(3)]

# Game loop
while True:
    print_board(board)
    board, won = make_move(board, move)
    if won:
        break
    new_board = [list(input().strip()) for _ in range(3)]
    board, won = make_move(new_board, move)
    if won:
        break
    board = new_board