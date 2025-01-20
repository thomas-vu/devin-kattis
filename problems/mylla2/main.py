def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != '_':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != '_':
            return board[0][i]
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    return None

def main():
    board = [list(input().strip()) for _ in range(3)]
    winner = check_winner(board)
    if winner == 'X':
        print("Jebb")
    elif winner == 'O':
        print("Neibb")
    else:
        print("Neibb")

if __name__ == "__main__":
    main()