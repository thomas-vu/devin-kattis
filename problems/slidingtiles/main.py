def rotate_tile(grid, letter):
    x = y = -1
    for i in range(5):
        for j in range(5):
            if grid[i][j] == letter:
                x, y = i, j
                break
    if x != -1 and y != -1:
        while x > 0 and grid[x-1][y] == ' ':
            x -= 1
        while y > 0 and grid[x][y-1] == ' ':
            y -= 1
        while x < 4 and grid[x+1][y] != ' ':
            if y > 0:
                grid[x][y], grid[x+1][y] = grid[x+1][y], grid[x][y]
            else:
                grid[x][y], grid[x+1][0] = grid[x+1][0], grid[x][y]
            x += 1
        while y < 4 and grid[x][y+1] != ' ':
            if x > 0:
                grid[x][y], grid[x-1][y] = grid[x-1][y], grid[x][y]
            else:
                grid[x][y], grid[x-1][4] = grid[x-1][4], grid[x][y]
            y += 1
    return grid

def process_moves(grid, moves):
    for move in moves:
        direction = move[-1]
        tile = move[:-2]
        if direction == 'U':
            grid = rotate_tile(grid, tile)
        elif direction == 'D':
            for _ in range(5):
                grid = rotate_tile(grid, tile)
        elif direction == 'L':
            for _ in range(5):
                grid = rotate_tile(grid, tile)
        elif direction == 'R':
            grid = rotate_tile(grid, tile)
    return grid

def main():
    while True:
        n = int(input())
        if n == -1:
            break
        grid = [[' ' for _ in range(5)] for _ in range(5)]
        letters = [chr(65 + i) for i in range(25)]
        index = 0
        for _ in range(n):
            move = input().split()
            grid[index // 5][index % 5] = letters[ord(move[1]) - ord('A')]
            index += 1
        moves = []
        for _ in range(n):
            move = input().split()
            moves.append(move[0])
        grid = process_moves(grid, moves)
        for row in grid:
            print(''.join(row).rstrip())
        print()

if __name__ == "__main__":
    main()