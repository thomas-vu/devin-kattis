def is_easy_sudoku(grid):
    def check_unique_location():
        for digit in range(1, 10):
            for row in range(9):
                if grid[row].count(digit) == 1:
                    col = grid[row].index(digit)
                    for i in range(9):
                        if i != row and digit in grid[i]:
                            break
                    else:
                        grid[row][col] = '.'
                        solved = True
                for col in range(9):
                    if [grid[row][col] for row in range(9)].count(digit) == 1:
                        row = [grid[row][col] for row in range(9)].index(digit)
                        for i in range(9):
                            if grid[i][col] != digit:
                                break
                        else:
                            grid[row][col] = '.'
                            solved = True
                for x in range(3):
                    for y in range(3):
                        sub_grid = [grid[i][j] for i in range(x*3, (x+1)*3) for j in range(y*3, (y+1)*3)]
                        if sub_grid.count(digit) == 1:
                            row = x*3 + sub_grid.index(digit) // 3
                            col = y*3 + sub_grid.index(digit) % 3
                            for i in range(x*3, (x+1)*3):
                                for j in range(y*3, (y+1)*3):
                                    if i != row or j != col:
                                        if digit in grid[i]:
                                            break
                            else:
                                grid[row][col] = '.'
                                solved = True
            if solved:
                break
        return solved

    def check_single_value():
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    possible_values = set(range(1, 10))
                    for i in range(9):
                        if grid[row][i] != 0:
                            possible_values.discard(grid[row][i])
                        if grid[i][col] != 0:
                            possible_values.discard(grid[i][col])
                    for i in range(3):
                        for j in range(3):
                            if grid[row//3*3+i][col//3*3+j] != 0:
                                possible_values.discard(grid[row//3*3+i][col//3*3+j])
                    if len(possible_values) == 1:
                        grid[row][col] = possible_values.pop()
                        solved = True
        return solved

    solved = False
    while not solved:
        solved = True
        for row in grid:
            if 0 in row:
                solved = False
                break
        if solved:
            break
        solved = check_unique_location() or check_single_value()
    return solved, grid

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    grid = [[int(x) for x in line] for line in data]
    solved, grid = is_easy_sudoku(grid)
    if solved:
        for row in grid:
            print(' '.join(str(x) if x != 0 else '.' for x in row))
    else:
        for row in grid:
            print(' '.join(str(x) if x != 0 else '.' for x in row))
        print('Not easy')

main()