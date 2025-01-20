MOD = 2**31 - 1
directions = [(0, 1), (1, 0)]  # right, down

def count_paths(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    
    if grid[0][0] == '#':
        return 0
    
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                dp[i][j] %= MOD
    
    return dp[-1][-1]

def can_reach(grid):
    n = len(grid)
    dp = [[False] * n for _ in range(n)]
    
    if grid[0][0] == '.':
        dp[0][0] = True
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '.':
                if i > 0:
                    dp[i][j] |= dp[i-1][j]
                if j > 0:
                    dp[i][j] |= dp[i][j-1]
    
    return dp[-1][-1]

def main():
    n = int(input().strip())
    grid = [input().strip() for _ in range(n)]
    
    paths_count = count_paths(grid)
    if paths_count > 0:
        print(paths_count)
    else:
        if can_reach(grid):
            print("THE GAME IS A LIE")
        else:
            print("INCONCEIVABLE")

if __name__ == "__main__":
    main()