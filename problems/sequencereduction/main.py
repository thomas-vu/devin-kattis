def min_cost_reducing(n, sequence):
    # Initialize a DP table where dp[i][j] represents the minimum cost to reduce subarray from i to j
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    
    # Base case: the cost to reduce a single element sequence is 0
    for i in range(n):
        dp[i][i] = 0
    
    # Fill the DP table using bottom-up approach
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            for k in range(i, j):
                cost = max(sequence[i:k+1]) + max(sequence[k+1:j+1])
                dp[i][j] = min(dp[i][j], cost + dp[i][k] + dp[k+1][j])
    
    return dp[0][n-1]

# Read input
n = int(input())
sequence = [int(input()) for _ in range(n)]

# Compute and print the result
print(min_cost_reducing(n, sequence))