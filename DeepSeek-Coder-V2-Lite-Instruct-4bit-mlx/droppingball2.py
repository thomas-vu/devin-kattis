def main():
    R, C, K = map(int, input().split())
    grid = [input() for _ in range(R)]
    scores = list(map(int, input().split()))
    
    # Initialize the dynamic programming table
    dp = [[0] * C for _ in range(K)]
    
    # Fill the dynamic programming table based on the grid and scores
    for j in range(C):
        if grid[R-1][j] == 'X' or grid[R-1][j] == '.':
            continue
        dp[0][j] = scores[j]
    
    for i in range(1, R):
        for j in range(C):
            if grid[R-i-1][j] == 'X':
                continue
            for k in range(K):
                if j > 0 and grid[R-i-1][j-1] in ('L', '?'):
                    dp[k+1][j-1] = max(dp[k+1][j-1], dp[k][j])
                if j < C-1 and grid[R-i-1][j+1] in ('R', '?'):
                    dp[k+1][j+1] = max(dp[k+1][j+1], dp[k][j])
    
    # Calculate the maximum score
    max_score = 0
    for k in range(K):
        for j in range(C):
            max_score = max(max_score, dp[k][j])
    
    print(max_score)

if __name__ == "__main__":
    main()