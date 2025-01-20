def is_possible(target, board):
    def find_pegs():
        pegs = []
        for i in range(4):
            for j in range(4 - i):
                if board[i][j] != '__':
                    pegs.append((i, j))
        return pegs

    def valid_moves(x, y):
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        moves = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 4 and 0 <= ny < 4 - (nx // 2):
                if board[nx][ny] != '__' and board[x + dx // 2][y + dy // 2] != '__':
                    moves.append(((x, y), (nx, ny)))
        return moves

    def make_move(x, y, nx, ny):
        board[x][y] = '__'
        board[nx][ny] = '__'
        board[x + dx // 2][y + dy // 2] = '__'

    def backtrack(moves):
        if len(find_pegs()) == 1:
            return board[0][0] == target
        for (x, y), (nx, ny) in moves:
            make_move(x, y, nx, ny)
            if backtrack(moves):
                return True
            make_move(nx, ny, x, y)  # backtrack
        return False

    moves = []
    for i in range(4):
        for j in range(4 - i):
            if board[i][j] != '__':
                for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < 4 and 0 <= ny < 4 - (nx // 2):
                        if board[nx][ny] != '__' and board[i + dx // 2][j + dy // 2] != '__':
                            moves.append((((i, j), (nx, ny))))
    return backtrack(moves)

while True:
    try:
        target = input().strip()
        board = [list(input().strip()) for _ in range(4)]
        if is_possible(target, board):
            print("Possible")
        else:
            print("Impossible")
    except EOFError:
        break