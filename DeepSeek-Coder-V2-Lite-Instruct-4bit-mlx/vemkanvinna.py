def can_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def main():
    board = [input().split() for _ in range(3)]
    
    x_count = sum([row.count('X') for row in board])
    o_count = sum([row.count('O') for row in board])
    
    if x_count == o_count + 1:
        johan_can_win = can_win(board, 'X')
    else:
        johan_can_win = False
    
    if x_count == o_count:
        abdullah_can_win = can_win(board, 'O')
    else:
        abdullah_can_win = False
    
    if johan_can_win and abdullah_can_win:
        print("Abdullah och Johan kan vinna")
    elif johan_can_win:
        print("Johan kan vinna")
    elif abdullah_can_win:
        print("Abdullah kan vinna")
    else:
        print("ingen kan vinna")

main()