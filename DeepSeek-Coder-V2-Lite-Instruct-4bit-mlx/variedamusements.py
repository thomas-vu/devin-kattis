MOD = 10**9 + 7

def count_sequences(n, a, b, c):
    # dp[i][j] represents the number of ways to choose i rides with the last ride being of type j
    dp = [[0] * 3 for _ in range(n + 1)]
    
    # Base cases: choosing 0 rides or 1 ride with any type is always 1
    for j in range(3):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        if i >= a:
            dp[i][0] = (dp[i][0] + dp[i - a][1]) % MOD
            dp[i][0] = (dp[i][0] + dp[i - a][2]) % MOD
        if i >= b:
            dp[i][1] = (dp[i][1] + dp[i - b][0]) % MOD
            dp[i][1] = (dp[i][1] + dp[i - b][2]) % MOD
        if i >= c:
            dp[i][2] = (dp[i][2] + dp[i - c][0]) % MOD
            dp[i][2] = (dp[i][2] + dp[i - c][1]) % MOD
    
    # The result is the sum of ways to end with any type of ride after n rides
    return (dp[n][0] + dp[n][1] + dp[n][2]) % MOD

# Read input
n, a, b, c = map(int, input().split())

# Output the result
print(count_sequences(n, a, b, c))