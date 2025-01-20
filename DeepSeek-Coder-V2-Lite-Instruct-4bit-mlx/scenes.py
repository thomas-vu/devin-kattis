MOD = 10**9 + 7

def count_scenes(n, w, h):
    # Initialize the DP array where dp[i] represents the number of ways to cover i columns
    dp = [0] * (w + 1)
    dp[0] = 1  # Base case: one way to cover zero columns (no ribbon used)
    
    for _ in range(1, h + 1):
        for i in range(w, -1, -1):
            # Calculate the number of ways to cover i columns with the current height
            for j in range(1, min(i // w + 1, n // h) + 1):
                dp[i] = (dp[i] + dp[i - j * w]) % MOD
    
    # The result is the sum of ways to cover all columns with height h
    return dp[w]

# Read input from stdin
n, w, h = map(int, input().split())

# Output the result
print(count_scenes(n, w, h))