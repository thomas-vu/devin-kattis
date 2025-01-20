def min_moving_cost(n, k, costs):
    # Initialize a DP table where dp[i][j] represents the minimum cost to service requests 1 to i using j teams
    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            min_cost = float('inf')
            for l in range(i + 1):
                min_cost = min(min_cost, dp[i - l][j - 1] + costs[i - l][l])
            dp[i][j] = min_cost

    return dp[n][k]

# Read input
import sys
input = sys.stdin.read
data = input().split()
n = int(data[0])
k = int(data[1])
costs = []
index = 2
for i in range(n):
    row = list(map(int, data[index:index + n - i]))
    costs.append(row)
    index += len(row)

# Calculate and print the minimum moving cost
result = min_moving_cost(n, k, costs)
print(result)