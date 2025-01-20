def sumdoku(grid):
    def is_valid(row, col, num):
        for i in range(9):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        for i in range(3):
            for j in range(3):
                if grid[row//3*3 + i][col//3*3 + j] == num:
                    return False
        return True

    def solve():
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(i, j, num):
                            grid[i][j] = num
                            if solve():
                                return True
                            grid[i][j] = 0
                    return False
        return True

    def print_grid():
        for row in grid:
            print(' '.join(map(str, row)))

    solve()
    return grid

# Input data parsing
input_data = [list(line.strip()) for line in open("sumdoku_input.txt")]
grid = [[0]*9 for _ in range(9)]

# Parsing constraints and filling the grid
for i in range(0, 15, 2):
    for j in range(9):
        if input_data[i][j] == '<':
            grid[i//2*3 + 0][(i+1)%9] = min((i+1)//9 + 1, (i+2)%9 + 1)
            grid[i//2*3 + 1][(i+1)%9] = min((i+1)//9 + 1, (i+2)%9 + 1)
            grid[i//2*3 + 2][(i+1)%9] = min((i+1)//9 + 1, (i+2)%9 + 1)
        elif input_data[i][j] == '=':
            grid[i//2*3 + 0][(i+1)%9] = (i+1)//9 + 1
            grid[i//2*3 + 1][(i+1)%9] = (i+1)//9 + 1
            grid[i//2*3 + 2][(i+1)%9] = (i+1)//9 + 1
        elif input_data[i][j] == '>':
            grid[i//2*3 + 0][(i+1)%9] = max((i+1)//9 + 1, (i+2)%9 + 1)
            grid[i//2*3 + 1][(i+1)%9] = max((i+1)//9 + 1, (i+2)%9 + 1)
            grid[i//2*3 + 2][(i+1)%9] = max((i+1)//9 + 1, (i+2)%9 + 1)
        if j < 8:
            j += 1
    for j in range(9):
        if input_data[i+1][j] == '<':
            grid[(i+1)//2*3 + 0][j] = min((i+2)//9 + 1, (i+3)%9 + 1)
            grid[(i+1)//2*3 + 1][j] = min((i+2)//9 + 1, (i+3)%9 + 1)
            grid[(i+1)//2*3 + 2][j] = min((i+2)//9 + 1, (i+3)%9 + 1)
        elif input_data[i+1][j] == '=':
            grid[(i+1)//2*3 + 0][j] = (i+2)//9 + 1
            grid[(i+1)//2*3 + 1][j] = (i+2)//9 + 1
            grid[(i+1)//2*3 + 2][j] = (i+2)//9 + 1
        elif input_data[i+1][j] == '>':
            grid[(i+1)//2*3 + 0][j] = max((i+2)//9 + 1, (i+3)%9 + 1)
            grid[(i+1)//2*3 + 1][j] = max((i+2)//9 + 1, (i+3)%9 + 1)
            grid[(i+1)//2*3 + 2][j] = max((i+2)//9 + 1, (i+3)%9 + 1)
        if j < 8:
            j += 1

# Solving the puzzle and printing the solution
solved_grid = sumdoku(grid)
for row in solved_grid:
    print(' '.join(map(str, row)))