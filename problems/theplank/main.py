def count_ways(n):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    elif n == 3:
        return 1
    
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 1, 1, 1
    
    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]

# Read input
n = int(input())
print(count_ways(n))