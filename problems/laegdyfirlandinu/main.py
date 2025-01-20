def check_low_pressure(grid, n, m):
    for i in range(1, n-1):
        for j in range(1, m-1):
            if grid[i][j] < min(grid[i+1][j], grid[i-1][j], grid[i][j+1], grid[i][j-1]):
                return "Jebb"
    return "Neibb"

def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    result = check_low_pressure(grid, n, m)
    print(result)

if __name__ == "__main__":
    main()