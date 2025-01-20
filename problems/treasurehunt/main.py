def find_treasure(R, C, grid):
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 'T':
                start_row, start_col = r, c
                break
    
    moves = 0
    current_row, current_col = start_row, start_col
    
    while 0 <= current_row < R and 0 <= current_col < C:
        if grid[current_row][current_col] == 'T':
            return moves
        elif grid[current_row][current_col] == 'N':
            current_row -= 1
        elif grid[current_row][current_col] == 'S':
            current_row += 1
        elif grid[current_row][current_col] == 'W':
            current_col -= 1
        elif grid[current_row][current_col] == 'E':
            current_col += 1
        moves += 1
    
    if not (0 <= current_row < R and 0 <= current_col < C):
        return "Out"
    else:
        return "Lost"

R, C = map(int, input().split())
grid = [input() for _ in range(R)]
result = find_treasure(R, C, grid)
print(result)