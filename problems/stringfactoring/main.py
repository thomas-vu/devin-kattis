def min_weight_factoring(s):
    n = len(s)
    
    # dp[i][j] will store the minimum weight of factoring substring s[i:j+1]
    dp = [[float('inf')] * n for _ in range(n)]
    
    # Base case: single character strings have a factoring weight of 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                current_cost = dp[i][k] + dp[k+1][j]
                if s[i:k+1] == s[k+1:j+1]:
                    current_cost = min(current_cost, 1 + (dp[i][k] if dp[i][k] != k - i + 1 else 0))
                dp[i][j] = min(dp[i][j], current_cost)
    
    return dp[0][n-1]

# Read input from stdin
s = input().strip()

# Get the minimum weight of the maximal factoring
result = min_weight_factoring(s)

# Output the result
print(result)