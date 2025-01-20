def max_score(n, points):
    # Initialize the DP array where dp[i] represents the maximum score ending at square i
    dp = [0] * n
    # The first square is always included in the score
    dp[0] = points[0]
    
    # Iterate through the squares to fill the DP array
    for i in range(1, n):
        # The maximum score ending at the current square is the best score of all previous squares
        # plus the points of the current square, but only if the jump is valid (non-decreasing)
        for j in range(i):
            if points[j] <= points[i]:  # Ensure the jump is non-decreasing
                dp[i] = max(dp[i], dp[j] + points[i])
    
    # The result is the maximum score in the last square
    return max(dp)

# Read input
n = int(input())
points = list(map(int, input().split()))

# Output the result
print(max_score(n, points))