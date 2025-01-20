def max_cash(N, T, people):
    # Sort the people based on the cash they have in descending order
    # If two people have the same amount of cash, sort by time they leave in ascending order
    people.sort(key=lambda x: (-x[0], x[1]))
    
    # Initialize the maximum cash to 0
    max_cash = 0
    
    # Use dynamic programming to find the maximum cash that can be collected
    dp = [0] * (T + 1)
    
    for cash, time in people:
        # Update the dp array with the current person's contribution
        for t in range(T, time, -1):
            dp[t] = max(dp[t], dp[t - 1] + cash)
    
    # The maximum amount of money is the last element in the dp array
    max_cash = dp[T]
    
    return max_cash

# Read input
N, T = map(int, input().split())
people = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
result = max_cash(N, T, people)
print(result)