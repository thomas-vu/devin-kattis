def min_operations_to_meow(s):
    n = len(s)
    dp = [[float('inf')] * 5 for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(n):
        for j in range(4):
            if dp[i][j] < float('inf'):
                # No operation
                if s[i] == 'm' and j == 0:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                elif s[i] == 'e' and j == 1:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                elif s[i] == 'o' and j == 2:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                elif s[i] == 'w' and j == 3:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
                else:
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
                
                # Insert
                for k in range(4):
                    dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + (0 if j == k else 1))
                
                # Delete
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
                
                # Replace
                for k in range(4):
                    if j != k:
                        dp[i + 1][j] = min(dp[i + 1][j], dp[i][k] + (0 if j == k else 1))
                
                # Swap
                if i < n - 1:
                    dp[i + 2][j] = min(dp[i + 2][j], dp[i][j] + (1 if s[i] == 'm' and s[i + 1] == 'e' and j == 0 else (2 if s[i] == 'm' and s[i + 1] == 'o' and j == 0 else (3 if s[i] == 'm' and s[i + 1] == 'w' and j == 0 else (4 if s[i] == 'e' and s[i + 1] == 'o' and j == 1 else (5 if s[i] == 'e' and s[i + 1] == 'w' and j == 1 else (6 if s[i] == 'o' and s[i + 1] == 'w' and j == 2 else float('inf')))))))))
    
    return min(dp[n][3], dp[n][2], dp[n][1], dp[n][0]) + 1

# Read input
s = input().strip()

# Compute and output the meow factor
print(min_operations_to_meow(s))