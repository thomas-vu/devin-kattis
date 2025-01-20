def move_left(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    merged = [[False] * 4 for _ in range(4)]
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                if pos != j:
                    merged[i][pos] = True
                pos += 1
    
    for i in range(4):
        for j in range(3):
            if new_grid[i][j] != 0 and new_grid[i][j] == new_grid[i][j + 1]:
                new_grid[i][j] *= 2
                new_grid[i][j + 1] = 0
                merged[i][j] = True
    
    for i in range(4):
        pos = 0
        for j in range(4):
            if new_grid[i][j] != 0:
                temp = new_grid[i][pos]
                new_grid[i][pos] = new_grid[i][j]
                if pos != j:
                    new_grid[i][j] = temp
                pos += 1
    
    return new_grid, merged

def move_up(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    merged = [[False] * 4 for _ in range(4)]
    
    for j in range(4):
        pos = 0
        for i in range(4):
            if grid[i][j] != 0:
                new_grid[pos][j] = grid[i][j]
                if pos != i:
                    merged[pos][j] = True
                pos += 1
    
    for j in range(4):
        for i in range(3):
            if new_grid[i][j] != 0 and new_grid[i][j] == new_grid[i + 1][j]:
                new_grid[i][j] *= 2
                new_grid[i + 1][j] = 0
                merged[i][j] = True
    
    for j in range(4):
        pos = 0
        for i in range(4):
            if new_grid[i][j] != 0:
                temp = new_grid[pos][j]
                new_grid[pos][j] = new_grid[i][j]
                if pos != i:
                    new_grid[i][j] = temp
                pos += 1
    
    return new_grid, merged

def move_right(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    merged = [[False] * 4 for _ in range(4)]
    
    for i in range(4):
        pos = 3
        for j in range(3, -1, -1):
            if grid[i][j] != 0:
                new_grid[i][pos] = grid[i][j]
                if pos != j:
                    merged[i][pos] = True
                pos -= 1
    
    for i in range(4):
        for j in range(3, 0, -1):
            if new_grid[i][j] != 0 and new_grid[i][j] == new_grid[i][j - 1]:
                new_grid[i][j] *= 2
                new_grid[i][j - 1] = 0
                merged[i][j] = True
    
    for i in range(4):
        pos = 3
        for j in range(3, -1, -1):
            if new_grid[i][j] != 0:
                temp = new_grid[i][pos]
                new_grid[i][pos] = new_grid[i][j]
                if pos != j:
                    new_grid[i][j] = temp
                pos -= 1
    
    return new_grid, merged

def move_down(grid):
    new_grid = [[0] * 4 for _ in range(4)]
    merged = [[False] * 4 for _ in range(4)]
    
    for j in range(4):
        pos = 3
        for i in range(3, -1, -1):
            if grid[i][j] != 0:
                new_grid[pos][j] = grid[i][j]
                if pos != i:
                    merged[pos][j] = True
                pos -= 1
    
    for j in range(4):
        for i in range(3, 0, -1):
            if new_grid[i][j] != 0 and new_grid[i][j] == new_grid[i - 1][j]:
                new_grid[i][j] *= 2
                new_grid[i - 1][j] = 0
                merged[i][j] = True
    
    for j in range(4):
        pos = 3
        for i in range(3, -1, -1):
            if new_grid[i][j] != 0:
                temp = new_grid[pos][j]
                new_grid[pos][j] = new_grid[i][j]
                if pos != i:
                    new_grid[i][j] = temp
                pos -= 1
    
    return new_grid, merged

def main():
    grid = [list(map(int, input().split())) for _ in range(4)]
    move = int(input())
    
    if move == 0:
        new_grid, merged = move_left(grid)
    elif move == 1:
        new_grid, merged = move_up(grid)
    elif move == 2:
        new_grid, merged = move_right(grid)
    elif move == 3:
        new_grid, merged = move_down(grid)
    
    for i in range(4):
        for j in range(4):
            if merged[i][j]:
                print(new_grid[i][j], end=' ')
            else:
                print(new_grid[i][j], end=' ') if j != 3 else print(new_grid[i][j])
        print()

if __name__ == "__main__":
    main()