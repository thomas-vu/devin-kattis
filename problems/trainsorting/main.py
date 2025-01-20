def longest_train(n, weights):
    # Initialize a DP array to store the length of the longest train ending with each car
    dp = [1] * n
    
    # Fill the DP array
    for i in range(n):
        for j in range(i):
            if weights[j] < weights[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The length of the longest train is the maximum value in dp array
    return max(dp)

# Read input
n = int(input())
weights = [int(input()) for _ in range(n)]

# Output the result
print(longest_train(n, weights))