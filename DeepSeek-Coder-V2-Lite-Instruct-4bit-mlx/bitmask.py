def min_cost_to_cover_data(binary_data, costs):
    n = len(binary_data)
    
    # dp[i] will store the minimum cost to cover the first i bits of the binary data
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    for i in range(1, n + 1):
        # Check all possible bitmasks of length i
        for j in range(i):
            mask = binary_data[j:i]
            if '0' in mask and '1' in mask:  # A valid bitmask must have both 0s and 1s
                continue
            cost = sum(costs[j:i]) + dp[j]
            dp[i] = min(dp[i], cost)
    
    return dp[n]

# Read input
binary_data = input().strip()
costs = list(map(int, input().split()))

# Calculate and output the minimum cost
print(min_cost_to_cover_data(binary_data, costs))