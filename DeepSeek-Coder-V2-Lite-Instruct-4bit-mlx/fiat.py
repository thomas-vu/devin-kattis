MOD = 10**9 + 7

def count_ways(N):
    # dp[i] represents the number of ways to divide i steps into rectangles
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    
    # The number of ways to divide N steps into rectangles is dp[N]
    return dp[N]

# Read input
N = int(input().strip())

# Calculate and output the result
result = count_ways(N)
print(result)