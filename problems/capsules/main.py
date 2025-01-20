def solve_sudoku(grid, rows, cols, regions):
    def is_valid(row, col, num):
        for i in range(cols):
            if grid[row][i] == num or grid[i][col] == num:
                return False
        region_row, region_col = row // (rows//3), col // (cols//3)
        for i in range(region_row * 3, region_row * 3 + 3):
            for j in range(region_col * 3, region_col * 3 + 3):
                if grid[i][j] == num:
                    return False
        return True

    def solve():
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '-':
                    for num in range(1, 10):
                        if is_valid(row, col, num):
                            grid[row][col] = num
                            if solve():
                                return True
                            grid[row][col] = '-'
                    return False
        return True

    solve()
    return grid

def main():
    R, C = map(int, input().split())
    grid = [list(input().strip()) for _ in range(R)]
    regions_count = int(input())
    regions = {}
    for _ in range(regions_count):
        region_info = list(map(int, input().split()))
        region_cells = []
        for _ in range(region_info[0]):
            cell_info = input().split(' (')
            row, col = map(int, cell_info[1].strip(')').split(','))
            region_cells.append((row - 1, col - 1))
        regions[region_info[1]] = region_cells
    
    for row in solve_sudoku(grid, R, C, regions):
        print(' '.join(str(x) for x in row))

if __name__ == "__main__":
    main()