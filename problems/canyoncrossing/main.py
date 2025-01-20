def read_ints():
    return list(map(int, input().split()))

R, C, K = read_ints()
canyon = []
for _ in range(R):
    canyon.append(read_ints())

# Initialize the DP table with infinity for unreachable cells
dp = [[float('inf')] * C for _ in range(R)]

# Set the starting points (bottom row) to their own height
for j in range(C):
    dp[R-1][j] = canyon[R-1][j]

# Use dynamic programming to find the minimum path height through the canyon
for i in range(R-2, -1, -1):
    for j in range(C):
        # Update the DP table from bottom to top, left to right
        if j > 0:
            dp[i][j] = min(dp[i][j], max(canyon[i][j], dp[i+1][j-1]))
        dp[i][j] = min(dp[i][j], max(canyon[i][j], dp[i+1][j]))
        if j < C-1:
            dp[i][j] = min(dp[i][j], max(canyon[i][j], dp[i+1][j+1]))

# Find the minimum path height at the top row after using bridges if possible
min_height = float('inf')
for j in range(C):
    min_height = min(min_height, canyon[0][j] - K)
    for l in range(1, min(K+1, R-1)):
        if j > 0:
            min_height = min(min_height, max(canyon[0][j] - K, dp[R-1-l][j-1]))
        min_height = min(min_height, max(canyon[0][j] - K, dp[R-1-l][j]))
        if j < C-1:
            min_height = min(min_height, max(canyon[0][j] - K, dp[R-1-l][j+1]))
        min_height = min(min_height, max(canyon[0][j] - K, dp[R-1-l][j]))

# Output the minimum height of the optimal path
print(min_height)