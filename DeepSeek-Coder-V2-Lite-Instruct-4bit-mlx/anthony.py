import sys
from math import comb

# Read input values
N, M = map(int, sys.stdin.readline().split())
# Read win probabilities for each round
p = [float(sys.stdin.readline().strip()) for _ in range(N + M - 1)]

# Dynamic programming to calculate probabilities of winning the game for Anthony
dp = [[0.0] * (M + 1) for _ in range(N + 1)]
dp[0][0] = 1.0

for i in range(N + 1):
    for j in range(M + 1):
        if i > 0:
            dp[i][j] += dp[i - 1][j] * (1.0 - p[i + j - 1])
        if j > 0:
            dp[i][j] += dp[i][j - 1] * p[i + j - 1]

# The probability of Anthony winning the game
ans = sum(dp[i][M - (N + i)] for i in range(N))
print("{:.9f}".format(ans))