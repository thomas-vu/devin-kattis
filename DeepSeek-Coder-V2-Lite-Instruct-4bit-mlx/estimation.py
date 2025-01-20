import sys
from itertools import accumulate

def min_error(A, k):
    n = len(A)
    dp = [[float('inf')] * (k+1) for _ in range(n+1)]
    prefix_sum = [0] + list(accumulate(A))
    
    def cost(l, r):
        mid = (l + r) // 2
        mean_value = (prefix_sum[r] - prefix_sum[l]) // (r - l)
        return sum(abs(A[i] - mean_value) for i in range(l, r))
    
    for i in range(1, n+1):
        dp[i][1] = cost(0, i)
        for j in range(2, min(i, k)+1):
            for x in range(j-1, i):
                dp[i][j] = min(dp[i][j], dp[x][j-1] + cost(x, i))
    
    return dp[n][k]

# Read input
n, k = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(n)]

# Calculate and output the minimum error
print(min_error(A, k))