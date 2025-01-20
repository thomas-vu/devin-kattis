def parse_octal(state):
    binary = format(int(state, 8), '027b')
    board = [binary[i:i+3] for i in range(0, 27, 3)]
    return board

def check_winner(board):
    for row in board:
        if all(cell == '1' for cell in row):
            return 'X wins'
        elif all(cell == '2' for cell in row):
            return 'O wins'
    for col in range(3):
        if all(row[col] == '1' for row in board):
            return 'X wins'
        elif all(row[col] == '2' for row in board):
            return 'O wins'
    if all(board[i][i] == '1' for i in range(3)):
        return 'X wins'
    elif all(board[i][i] == '2' for i in range(3)):
        return 'O wins'
    if all(board[i][2-i] == '1' for i in range(3)):
        return 'X wins'
    elif all(board[i][2-i] == '2' for i in range(3)):
        return 'O wins'
    if any('0' in row for row in board):
        return 'In progress'
    return 'Cat\'s'

def main():
    c = int(input())
    for _ in range(c):
        state = input().strip()
        board = parse_octal(state)
        result = check_winner(board)
        print(result)

if __name__ == "__main__":
    main()