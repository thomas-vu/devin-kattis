def min_pegs_and_moves(board):
    def count_pegs():
        return sum(row.count('o') for row in board)
    
    def make_move(x, y):
        if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == 'o':
            dx = x - peg_positions[0][0]
            dy = y - peg_positions[0][1]
            jump_x = x + dx
            jump_y = y + dy
            if 0 <= jump_x < len(board) and 0 <= jump_y < len(board[0]) and board[jump_x][jump_y] == '.':
                new_board = [list(row) for row in board]
                new_board[peg_positions[0][0]][peg_positions[0][1]] = '.'
                new_board[x][y] = '.'
                new_board[jump_x][jump_y] = 'o'
                return new_board, 1
        return board, 0
    
    def dfs(moves):
        nonlocal min_pegs, min_moves
        if count_pegs() < min_pegs:
            min_pegs = count_pegs()
            min_moves = moves
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'o':
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_board, added = make_move(i + dx, j + dy)
                        if added:
                            dfs(moves + 1)
                            board = new_board
    
    min_pegs = float('inf')
    min_moves = float('inf')
    
    for case in range(N):
        board = []
        while True:
            line = input().strip()
            if not line:
                break
            board.append(list(line))
        
        peg_positions = [(i, j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == 'o']
        dfs(0)
        
        print(min_pegs, min_moves)