MOD = 1000000009

def count_ways(N, K, T):
    if T < N or T > N * K:
        return 0
    
    # Initialize the DP table
    dp = [[0] * (T + 1) for _ in range(N + 1)]
    dp[0][0] = 1
    
    for i in range(1, N + 1):
        for j in range(T + 1):
            for k in range(1, K + 1):
                if j - k >= 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
    
    return dp[N][T]

# Read input
import sys
input = sys.stdin.read
data = input().split()
index = 0
N = int(data[index])
K = int(data[index + 1])
T = int(data[index + 2])
index += 3

# Output the result
print(count_ways(N, K, T))