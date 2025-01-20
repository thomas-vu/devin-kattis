def min_sum_of_squared_errors(d, k, pixels):
    from itertools import accumulate
    
    # Flatten the list of pixels into a single list of red values
    red_values = [r for r, p in pixels for _ in range(p)]
    
    # Sort the red values to ensure they are in increasing order
    red_values.sort()
    
    # Create a cumulative sum array for the red values
    cum_sum = [0] + list(accumulate(red_values))
    
    # Precompute the sum of squared errors for each possible set of k integers
    dp = [[float('inf')] * (d + 1) for _ in range(k + 1)]
    dp[0][0] = 0
    
    for i in range(1, k + 1):
        for j in range(i, d + 1):
            min_error = float('inf')
            for l in range(i - 1, j):
                error = (red_values[j - 1] * (j - l) - (cum_sum[j] - cum_sum[l]))
                min_error = min(min_error, error)
            dp[i][j] = min(dp[i][j], dp[i - 1][l] + min_error)
    
    return dp[k][d]

# Read the input
import sys
input = sys.stdin.read
data = input().split()

# Parse the data
d = int(data[0])
k = int(data[1])
pixels = []
index = 2
for _ in range(d):
    r = int(data[index])
    p = int(data[index + 1])
    pixels.append((r, p))
    index += 2

# Compute and print the result
result = min_sum_of_squared_errors(d, k, pixels)
print(result)