def can_reach_end(N, railway):
    # Dynamic programming to track if it's possible to reach each position on the railway
    dp = [[False] * 3 for _ in range(N)]
    
    # Initial position on the first row is always valid if it's a rail
    for j in range(3):
        if railway[0][j] == '.':
            dp[0][j] = True
    
    # Fill the dynamic programming table
    for i in range(1, N):
        for j in range(3):
            if railway[i][j] == '.':
                for k in range(-1, 2):
                    if j + k >= 0 and j + k < 3:
                        if railway[i - 1][j + k] == '.' or railway[i - 1][j + k] == '/' and j + k > 0:
                            dp[i][j] = True
                        if railway[i - 1][j + k] == '*' and (j + k > 0 or railway[i - 1][j + k - 1] == '/'):
                            dp[i][j] = True
                        if railway[i - 1][j + k] == '/' and (j + k < 2 or railway[i - 1][j + k + 1] == '*'):
                            dp[i][j] = True
    
    # Check if it's possible to reach the last row
    return "YES" if any(dp[N - 1]) else "NO"

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
railway = data[1:]

# Output the result
print(can_reach_end(N, railway))