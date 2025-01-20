def min_inserted_length(before, after):
    n = len(after)
    m = len(before)
    
    # Initialize the minimum length of inserted DNA to a large number
    min_inserted = float('inf')
    
    # Use dynamic programming to find the minimum length of inserted DNA
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dynamic programming table
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if before[i - 1] == after[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    
    # The minimum length of inserted DNA is the difference in lengths plus the edit distance
    min_inserted = dp[m][n] - (n - m)
    
    return min_inserted

# Read input from stdin
import sys
before = input().strip()
after = input().strip()

# Get the minimum length of inserted DNA
result = min_inserted_length(before, after)

# Output the result
print(result)