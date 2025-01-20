def count_flips(grid):
    def flip(x, y):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                grid[nx][ny] = '1' if grid[nx][ny] == '0' else '0'
    
    def is_all_white(grid):
        for row in grid:
            if '0' in row:
                return False
        return True
    
    def copy_grid(grid):
        return [row[:] for row in grid]
    
    min_flips = float('inf')
    initial_grid = [['0' if cell == '.' else '1' for cell in row] for row in grid]
    
    def backtrack(flips, x, y):
        nonlocal min_flips
        if is_all_white(initial_grid):
            min_flips = min(min_flips, flips)
            return
        if x == 3:
            backtrack(flips, 0, y + 1)
            return
        if y == 3:
            backtrack(flips, x + 1, 0)
            return
        backup = copy_grid(initial_grid)
        flip(x, y)
        backtrack(flips + 1, x, y + 1)
        initial_grid = backup
    
    backtrack(0, 0, 0)
    return min_flips

def main():
    P = int(input().strip())
    for _ in range(P):
        grid = [list(input().strip()) for _ in range(3)]
        print(count_flips(grid))

if __name__ == "__main__":
    main()