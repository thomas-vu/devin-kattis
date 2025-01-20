def max_probability(probabilities):
    n = len(probabilities)
    dp = [0.0] * (1 << n)
    dp[0] = 1.0
    
    for mask in range(1 << n):
        count = bin(mask).count('1')
        for i in range(n):
            if (mask & (1 << i)) == 0:
                new_mask = mask | (1 << i)
                dp[new_mask] = max(dp[new_mask], dp[mask] * probabilities[count][i] / 100)
    
    return dp[(1 << n) - 1] * 100

# Read input
n = int(input())
probabilities = []
for _ in range(n):
    row = list(map(int, input().split()))
    probabilities.append(row)

# Calculate and output the result
result = max_probability(probabilities)
print("{:.10f}".format(result))