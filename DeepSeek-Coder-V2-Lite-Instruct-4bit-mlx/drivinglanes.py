n, m = map(int, input().split())
k, r = map(int, input().split())
straights = [int(input()) for _ in range(n)]
curves = [list(map(int, input().split())) for _ in range(n - 1)]

# Initialize the DP array to store the minimum distance for each lane and position
dp = [[float('inf')] * n for _ in range(m + 1)]
dp[1][0] = 0

for i in range(n):
    for j in range(1, m + 1):
        # Stay in the current lane
        if i > 0:
            dp[j][i] = min(dp[j][i], dp[j][i - 1] + straights[i])
        # Change to the adjacent lane and stay there
        if j > 1:
            dp[j][i] = min(dp[j][i], dp[j - 1][i - 1] + straights[i])
        # Change to the adjacent lane and stay there with reduced distance due to curve
        if i > 0:
            for l in range(1, m + 1):
                if j == l:
                    dp[l][i] = min(dp[l][i], dp[l][i - 1] + straights[i])
                else:
                    dp[l][i] = min(dp[l][i], dp[l][i - 1] + straights[i] + k + r * abs(j - l))

# The minimum distance to travel is the minimum of the last lane's distances
print(min(dp[j][n - 1] for j in range(1, m + 1)))