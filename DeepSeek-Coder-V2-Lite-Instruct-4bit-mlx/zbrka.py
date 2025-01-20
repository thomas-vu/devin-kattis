MOD = 1_000_000_007

def count_sequences(N, C):
    # Create a DP table where dp[i][j] represents the number of sequences
    # of length i with confusion j.
    dp = [[0] * (C + 1) for _ in range(N + 1)]
    
    # Base case: there is exactly one sequence of length 0 with confusion 0.
    dp[0][0] = 1
    
    # Fill the DP table
    for i in range(1, N + 1):
        for j in range(C + 1):
            # For each position, we can either include the number i or not.
            dp[i][j] = (dp[i - 1][j] * i) % MOD
            if j > 0:
                # Subtract the number of ways to achieve confusion j without including i.
                dp[i][j] = (dp[i][j] - dp[i - 1][j - 1]) % MOD
    
    return dp[N][C]

# Read input
N, C = map(int, input().split())
result = count_sequences(N, C)
print(result)