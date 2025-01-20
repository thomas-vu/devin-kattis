def simulate_days(grid, r, c):
    while True:
        new_grid = [['' for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'R':
                    new_grid[i][j] = ('R' if grid[i][j+1] != 'P' and grid[i][j-1] != 'P' and grid[i+1][j] != 'P' and grid[i-1][j] != 'P' else
                                      ('S' if grid[i][j+1] == 'S' or grid[i][j-1] == 'S' or grid[i+1][j] == 'S' or grid[i-1][j] == 'S' else
                                       'P')))
                elif grid[i][j] == 'S':
                    new_grid[i][j] = ('S' if grid[i][j+1] != 'R' and grid[i][j-1] != 'R' and grid[i+1][j] != 'R' and grid[i-1][j] != 'R' else
                                      ('P' if grid[i][j+1] == 'P' or grid[i][j-1] == 'P' or grid[i+1][j] == 'P' or grid[i-1][j] == 'P' else
                                       'R')))
                elif grid[i][j] == 'P':
                    new_grid[i][j] = ('P' if grid[i][j+1] != 'S' and grid[i][j-1] != 'S' and grid[i+1][j] != 'S' and grid[i-1][j] != 'S' else
                                      ('R' if grid[i][j+1] == 'R' or grid[i][j-1] == 'R' or grid[i+1][j] == 'R' or grid[i-1][j] == 'R' else
                                       'S')))
        if new_grid == grid:
            break
        grid = new_grid
    return grid

def main():
    t = int(input())
    for _ in range(t):
        r, c, n = map(int, input().split())
        grid = [list(input().strip()) for _ in range(r)]
        for day in range(n):
            grid = simulate_days(grid, r, c)
        for row in grid:
            print(''.join(row))
        if _ != t - 1:
            input()

if __name__ == "__main__":
    main()