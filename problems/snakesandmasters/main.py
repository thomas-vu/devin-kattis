MOD = 10**6

def count_ways(N):
    if N == 1:
        return 1
    elif N == 2:
        return 2
    
    dp = [0] * (N + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, N + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
    
    return dp[N]

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])

# Output the result
print(count_ways(N))