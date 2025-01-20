def expected_height(N, probabilities):
    # dp[i][j] will store the expected height of the tower if we have i face-up blocks and j face-down blocks
    dp = [[0.0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: if there are no blocks, the height is 0
    dp[0][0] = 0.0
    
    # Fill the DP table
    for i in range(N + 1):
        for j in range(N + 1):
            if i + j == N:  # All blocks are placed
                continue
            
            total_blocks = i + j
            if i > j:  # If there are more face-up blocks than face-down blocks
                prob_up = probabilities[N - total_blocks - 1]
                expected_height_with_up = dp[i + 1][j] if i + 1 <= N else 0.0
                expected_height_with_down = dp[i][j + 1] if j + 1 <= N else 0.0
                dp[i][j] = (prob_up * expected_height_with_down + (1 - prob_up) * expected_height_with_up) / total_blocks
            else:  # If there are more face-down blocks than face-up blocks or equal
                prob_down = probabilities[N - total_blocks - 1]
                expected_height_with_up = dp[i + 1][j] if i + 1 <= N else 0.0
                expected_height_with_down = dp[i][j + 1] if j + 1 <= N else 0.0
                dp[i][j] = (prob_down * expected_height_with_up + (1 - prob_down) * expected_height_with_down) / total_blocks
    
    return dp[0][0]

# Read input
N = int(input())
probabilities = [float(input()) for _ in range(N)]

# Calculate and output the expected height of the stable tower
result = expected_height(N, probabilities)
print("{:.10f}".format(result))