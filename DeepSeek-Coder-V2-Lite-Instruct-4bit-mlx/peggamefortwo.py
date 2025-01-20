def calculate_score(board):
    score = 0
    for i in range(5):
        for j in range(i + 1):
            score += board[i][j]
    return score

def make_jump(board, x, y, player):
    value = board[x][y]
    jumps = []
    
    # Check for vertical jump
    if x + 2 < 5 and board[x + 1][y] != 0 and board[x + 2][y] == 0:
        jumps.append((x + 2, y, x + 1, y))
    
    # Check for horizontal jump (left)
    if y - 2 >= 0 and board[x][y - 1] != 0 and board[x][y - 2] == 0:
        jumps.append((x, y - 2, x, y - 1))
    
    # Check for horizontal jump (right)
    if y + 2 < 5 and board[x][y + 1] != 0 and board[x][y + 2] == 0:
        jumps.append((x, y + 2, x, y + 1))
    
    # Check for diagonal jump (up-left)
    if x - 2 >= 0 and y - 2 >= 0 and board[x - 1][y - 1] != 0 and board[x - 2][y - 2] == 0:
        jumps.append((x - 2, y - 2, x - 1, y - 1))
    
    # Check for diagonal jump (up-right)
    if x - 2 >= 0 and y + 2 < 5 and board[x - 1][y + 1] != 0 and board[x - 2][y + 2] == 0:
        jumps.append((x - 2, y + 2, x - 1, y + 1))
    
    # Check for diagonal jump (down-left)
    if x + 2 < 5 and y - 2 >= 0 and board[x + 1][y - 1] != 0 and board[x + 2][y - 2] == 0:
        jumps.append((x + 2, y - 2, x + 1, y - 1))
    
    # Check for diagonal jump (down-right)
    if x + 2 < 5 and y + 2 < 5 and board[x + 1][y + 1] != 0 and board[x + 2][y + 2] == 0:
        jumps.append((x + 2, y + 2, x + 1, y + 1))
    
    best_jump = None
    max_score = -float('inf') if player == 0 else float('inf')
    
    for jump in jumps:
        new_board = [row[:] for row in board]
        new_board[x][y] = 0
        new_board[jump[0]][jump[1]] = 0
        new_board[jump[2]][jump[3]] = value
        score = calculate_score(new_board)
        if player == 0:
            next_score = minimax(new_board, depth + 1, True)
            if next_score > max_score:
                max_score = next_score
                best_jump = jump
        else:
            next_score = minimax(new_board, depth + 1, False)
            if next_score < max_score:
                max_score = next_score
                best_jump = jump
    
    if best_jump is not None:
        x, y, new_x, new_y = best_jump
        board[x][y] = 0
        board[new_x][new_y] = value
        return True, board
    return False, board

def minimax(board, depth, is_maximizing):
    if depth == 5:
        return calculate_score(board)
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(5):
            for j in range(i + 1):
                if board[i][j] != 0:
                    made_jump, new_board = make_jump(board, i, j, 0)
                    if made_jump:
                        score = minimax(new_board, depth + 1, False)
                        best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(5):
            for j in range(i + 1):
                if board[i][j] != 0:
                    made_jump, new_board = make_jump(board, i, j, 1)
                    if made_jump:
                        score = minimax(new_board, depth + 1, True)
                        best_score = min(best_score, score)
        return best_score

def main():
    board = []
    for _ in range(5):
        row = list(map(int, input().split()))
        board.append(row)
    
    jacquez_score = 0
    alia_score = 0
    player = 0
    
    while True:
        made_jump, new_board = make_jump(board, player == 0)
        if not made_jump:
            break
        board = new_board
        player = 1 - player
    
    jacquez_score = calculate_score(board)
    alia_score = calculate_score([[0 for _ in range(i + 1)] for i in range(5)])
    print(jacquez_score - alia_score)

if __name__ == "__main__":
    main()