def min_cost_to_reach_square(N, fees):
    # Create a list to store the minimum cost to reach each square
    dp = [float('inf')] * (N + 1)
    dp[1] = 0  # Base case: starting from square 1 with no cost

    for i in range(2, N + 1):
        # Check forward jump from the previous square
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + fees[i - 1])
        # Check backward jump from the previous square
        if i > 2:
            dp[i] = min(dp[i], dp[i - 1] + fees[i - 2])

    return dp[N]

# Read input
N = int(input().strip())
fees = [int(input().strip()) for _ in range(N)]

# Calculate and output the result
print(min_cost_to_reach_square(N, fees))