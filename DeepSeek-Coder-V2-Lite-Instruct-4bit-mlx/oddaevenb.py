MOD = 10**9 + 7

def count_songs(n):
    # Initialize the DP arrays for even and odd counts of 'a' and 'b'
    dp = [[[0] * 2 for _ in range(2)] for __ in range(n + 1)]
    
    # Base case: no notes
    dp[0][0][0] = 1
    
    for i in range(1, n + 1):
        # Update the counts for 'a' and 'b' being even or odd
        dp[i][0][0] = (dp[i - 1][1][1]) % MOD
        dp[i][0][1] = (dp[i - 1][1][0] + dp[i - 1][0][1]) % MOD
        dp[i][1][0] = (dp[i - 1][0][0] + dp[i - 1][1][0]) % MOD
        dp[i][1][1] = (dp[i - 1][0][1]) % MOD
    
    # The total number of valid songs is the sum of counts for even 'a' and odd 'b'
    return (dp[n][0][0] + dp[n][1][1]) % MOD

# Read the input
n = int(input().strip())
print(count_songs(n))