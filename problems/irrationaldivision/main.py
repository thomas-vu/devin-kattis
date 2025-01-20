def max_happiness_difference(p, q):
    # Create a DP table to store the maximum difference of happiness
    dp = [[0] * (q + 1) for _ in range(p + 1)]
    
    # Fill the DP table
    for i in range(1, p + 1):
        for j in range(1, q + 1):
            # If the current position is on a dark square (i+j)%2==0
            if (i + j) % 2 == 0:
                # The difference is increased by taking the square
                dp[i][j] = max(dp[i-1][j] + (0 if (i-1+j)%2==0 else 1), dp[i][j-1] + (0 if (i+j-1)%2==0 else 1))
            else:
                # The difference is decreased by taking the square
                dp[i][j] = max(dp[i-1][j] + (1 if (i-1+j)%2==0 else 0), dp[i][j-1] + (1 if (i+j-1)%2==0 else 0))
    
    # The result is the maximum difference in the bottom-right cell
    return dp[p][q] - (p * q // 2 - dp[p][q])

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
p, q = int(data[0]), int(data[1])

# Calculate and print the result
print(max_happiness_difference(p, q))