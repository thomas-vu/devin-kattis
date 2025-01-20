def find_islands(grid, r, c):
    def dfs(x, y):
        if x < 0 or x >= r or y < 0 or y >= c or grid[x][y] != 'L':
            return
        grid[x][y] = '#'  # Mark as visited
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)

    islands = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'L':
                dfs(i, j)
                islands += 1
    return islands

def main():
    while True:
        try:
            r, c = map(int, input().split())
            grid = [list(input().strip()) for _ in range(r)]
            result = find_islands(grid, r, c)
            print(result)
        except EOFError:
            break

if __name__ == "__main__":
    main()