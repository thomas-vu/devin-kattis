def is_valid_solution(board):
    n = 8
    queens = []
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == '*':
                queens.append((i, j))
    
    if len(queens) != n:
        return "invalid"
    
    for i in range(n):
        for j in range(i + 1, n):
            (x1, y1), (x2, y2) = queens[i], queens[j]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return "invalid"
    
    return "valid"

board = [input().strip() for _ in range(8)]
print(is_valid_solution(board))