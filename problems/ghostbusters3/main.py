MOD = 10**9 + 7

def count_ways(n, m):
    # Create a list to store the number of ways for each ghost count
    dp = [0] * (m + 1)
    
    # Base case: If there are no Ghostbusters, the number of ways is 1
    dp[0] = 1
    
    # Calculate the number of ways for each possible number of Ghostbusters
    for i in range(1, n + 1):
        new_dp = [0] * (m + 1)
        for j in range(1, m + 1):
            new_dp[j] = (new_dp[j - 1] * i + dp[j]) % MOD
        dp = new_dp
    
    # The final answer is the number of ways to assign ghosts when all n Ghostbusters are used
    return dp[m]

# Read input from stdin
n, m = map(int, input().split())

# Output the result
print(count_ways(n, m))