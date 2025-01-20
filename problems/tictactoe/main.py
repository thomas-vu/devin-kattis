def check_winner(board, n, m):
    # Check rows and columns
    for i in range(n):
        row = board[i]
        col = ''.join([board[j][i] for j in range(n)])
        if row.find('X' * m) != -1:
            return 'X WINS'
        if row.find('O' * m) != -1:
            return 'O WINS'
        if col.find('X' * m) != -1:
            return 'X WINS'
        if col.find('O' * m) != -1:
            return 'O WINS'
    
    # Check diagonals
    diag1 = ''.join([board[i][i] for i in range(n)])
    diag2 = ''.join([board[i][n - 1 - i] for i in range(n)])
    if diag1.find('X' * m) != -1 or diag2.find('X' * m) != -1:
        return 'X WINS'
    if diag1.find('O' * m) != -1 or diag2.find('O' * m) != -1:
        return 'O WINS'
    
    # Check for draw or in progress
    if '.' not in ''.join(board):
        return 'DRAW'
    else:
        return 'IN PROGRESS'

def main():
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]
    
    result = check_winner(board, n, m)
    print(result)

if __name__ == "__main__":
    main()