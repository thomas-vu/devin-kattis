import sys
from math import fsum, exp

# Read input
N, M, K = map(int, sys.stdin.readline().split())
logs = [tuple(map(float, sys.stdin.readline().split())) for _ in range(M)]

# Initialize DP array with -1 (unvisited states)
dp = [[-1.0 for _ in range(N + 1)] for _ in range(M + 1)]
dp[0][0] = 0.0

# Function to calculate expected time using dynamic programming
def expected_time(n, m):
    if n == 0:
        return 0.0
    if dp[m][n] != -1.0:
        return dp[m][n]
    
    time_to_place = logs[m - 1][0]
    prob_combust = logs[m - 1][1]
    
    # Expected time if the log does not combust
    dont_combust = expected_time(n, m + 1) + time_to_place
    
    # Expected time if the log combusts and waits for K seconds
    wait_time = expected_time(n - 1, m) + time_to_place + K
    
    # Probability that the log does not combust and probability that it does
    prob_not_combust = (1.0 - prob_combust)
    prob_combust = prob_combust
    
    # Expected time considering both scenarios with probabilities
    expected = (prob_not_combust * dont_combust) + (prob_combust * wait_time)
    
    dp[m][n] = expected
    return expected

# Calculate the expected time for building N logs
result = expected_time(N, 0)
print("{:.12f}".format(result))