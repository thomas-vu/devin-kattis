def min_keystrokes(s1, s2):
    n = len(s1)
    m = len(s2)
    
    # Initialize DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        dp[i][0] = i
    for j in range(1, m + 1):
        dp[0][j] = j
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Replace, insert, or delete character
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[n][m]

# Read inputs
import sys
input = sys.stdin.read
data = input().split()
s1 = data[0]
s2 = data[1]

# Calculate and output the result
result = min_keystrokes(s1, s2)
print(result)