def draw_minesweeper(n, m, k, mines):
    board = [['.' for _ in range(m)] for _ in range(n)]
    for y, x in mines:
        board[y-1][x-1] = '*'
    for y in range(n):
        for x in range(m):
            if board[y][x] == '.':
                count = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if dy == 0 and dx == 0:
                            continue
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] == '*':
                            count += 1
                board[y][x] = str(count)
    for row in board:
        print(''.join(row))

# Read input
n, m, k = map(int, input().split())
mines = [tuple(map(int, input().split())) for _ in range(k)]

# Draw the Minesweeper board
draw_minesweeper(n, m, k, mines)