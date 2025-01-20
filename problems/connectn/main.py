def check_winner(board, n):
    rows = len(board)
    cols = len(board[0])
    
    # Check horizontal, vertical, and both diagonals for a win
    def check_line(line):
        count = 0
        for disc in line:
            if disc == 'R':
                count += 1
                if count == n:
                    return 'RED'
            else:
                count = 0
        return None
    
    for row in board:
        winner = check_line(row)
        if winner:
            return winner
    
    for col in range(cols):
        column = [board[row][col] for row in range(rows)]
        winner = check_line(column)
        if winner:
            return winner
    
    # Check diagonals /
    for row in range(rows):
        for col in range(cols):
            if row + n <= rows and col + n <= cols:
                diagonal = [board[row+i][col+i] for i in range(n)]
                winner = check_line(diagonal)
                if winner:
                    return winner
    
    # Check diagonals \
    for row in range(rows):
        for col in range(cols):
            if row + n <= rows and col - n + 1 >= 0:
                diagonal = [board[row+i][col-i] for i in range(n)]
                winner = check_line(diagonal)
                if winner:
                    return winner
    
    return 'NONE'

# Read input
x, y, n = map(int, input().split())
board = [input().split() for _ in range(x)]

# Check and print the winner
winner = check_winner(board, n)
print(winner + ' WINS') if winner != 'NONE' else print('NONE')