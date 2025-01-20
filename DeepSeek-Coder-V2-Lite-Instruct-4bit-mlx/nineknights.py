def is_valid_knight(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == 'k':
                # Check all possible knight moves
                if i+2 < 5 and j+1 < 5 and board[i+2][j+1] == 'k':
                    return False
                if i+2 < 5 and j-1 >= 0 and board[i+2][j-1] == 'k':
                    return False
                if i-2 >= 0 and j+1 < 5 and board[i-2][j+1] == 'k':
                    return False
                if i-2 >= 0 and j-1 >= 0 and board[i-2][j-1] == 'k':
                    return False
                if i+1 < 5 and j+2 < 5 and board[i+1][j+2] == 'k':
                    return False
                if i+1 < 5 and j-2 >= 0 and board[i+1][j-2] == 'k':
                    return False
                if i-1 >= 0 and j+2 < 5 and board[i-1][j+2] == 'k':
                    return False
                if i-1 >= 0 and j-2 >= 0 and board[i-1][j-2] == 'k':
                    return False
    return True

def main():
    board = [input().strip() for _ in range(5)]
    if is_valid_knight(board):
        print("valid")
    else:
        print("invalid")

if __name__ == "__main__":
    main()