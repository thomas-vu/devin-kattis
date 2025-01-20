def count_captures(board):
    captures = 0
    directions = [(1, -1), (1, 1)]  # Right-up and right-down for light pieces

    for i in range(10):
        for j in range(10):
            if board[i][j] == 'W':
                for dx, dy in directions:
                    x, y = i + 2 * dx, j + 2 * dy
                    if 0 <= x < 10 and 0 <= y < 10:
                        if board[x][y] == 'B' and board[i + dx][j + dy] == '.':
                            captures += 1
    return captures

def main():
    T = int(input())
    for _ in range(T):
        input()  # Empty line
        board = [input().strip() for _ in range(10)]
        print(count_captures(board))

if __name__ == "__main__":
    main()