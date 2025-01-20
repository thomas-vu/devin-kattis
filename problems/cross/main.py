def is_valid(grid):
    for row in grid:
        if any(row.count(str(i)) > 1 for i in range(1, 10)):
            return False
    for col in zip(*grid):
        if any(col.count(str(i)) > 1 for i in range(1, 10)):
            return False
    boxes = [[] for _ in range(9)]
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            boxes[i // 3 * 3 + j // 3].append(val)
    for box in boxes:
        if any(box.count(str(i)) > 1 for i in range(1, 10)):
            return False
    return True

def cross_hatching(grid):
    while True:
        changes = False
        for num in range(1, 10):
            positions = []
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == str(num):
                        positions.append((i, j))
            for pos in positions:
                row, col = pos
                box_row, box_col = 3 * (row // 3), 3 * (col // 3)
                box = [grid[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                if grid[row].count('.') == 1 and '.' in box:
                    for j in range(9):
                        if grid[row][j] == '.':
                            box = [grid[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                            if str(num) not in box:
                                grid[row] = list(grid[row])
                                grid[row][j] = str(num)
                                changes = True
                if grid[col].count('.') == 1 and '.' in box:
                    for i in range(9):
                        if grid[i][col] == '.':
                            box = [grid[r][c] for r in range(box_row, box_row + 3) for c in range(box_col, box_col + 3)]
                            if str(num) not in box:
                                grid[i][col] = str(num)
                                changes = True
                if box.count('.') == 1 and '.' in box:
                    for r in range(box_row, box_row + 3):
                        for c in range(box_col, box_col + 3):
                            if grid[r][c] == '.':
                                box = [grid[r_][c_] for r_ in range(box_row, box_row + 3) for c_ in range(box_col, box_col + 3)]
                                if str(num) not in box:
                                    grid[r][c] = str(num)
                                    changes = True
            if not changes:
                break
        else:
            continue
        break
    return grid

def main():
    grid = [list(input().strip()) for _ in range(9)]
    if not is_valid(grid):
        print("ERROR")
        return
    solved_grid = cross_hatching(grid)
    if not is_valid(solved_grid):
        print("ERROR")
    else:
        for row in solved_grid:
            print(''.join(row))

if __name__ == "__main__":
    main()