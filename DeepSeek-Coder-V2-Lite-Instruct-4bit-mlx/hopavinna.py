def min_time_to_pass(n, assignments):
    # Initialize a list to store the minimum time needed to pass each assignment
    dp = [0] * n
    
    # Base case: if no assignments, the minimum time is 0
    if n == 0:
        return 0
    
    # Fill the dp array based on the given conditions
    for i in range(n):
        if i == 0:
            dp[i] = assignments[i]
        elif i == 1:
            dp[i] = min(assignments[i], assignments[i - 1])
        else:
            # Either participate in the current assignment or skip it and take the previous one's minimum time
            dp[i] = min(dp[i - 1], dp[i - 2]) + assignments[i]
    
    # The answer is the minimum time needed to pass the last assignment
    return dp[-1]

# Read input from stdin
n = int(input())
assignments = list(map(int, input().split()))

# Output the result
print(min_time_to_pass(n, assignments))