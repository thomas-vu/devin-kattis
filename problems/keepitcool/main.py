def refill_sodas(n, m, s, d, current):
    # Calculate the total number of sodas needed in each slot to achieve the maximum probability
    required = [max(0, d - c) for c in current]
    
    # Check if the total number of sodas needed exceeds the available new bottles
    if sum(required) > n:
        return "impossible"
    
    # Distribute the new bottles to each slot to maximize the probability of getting a cold soda
    distribution = [0] * s
    for i in range(s):
        if required[i] <= n:
            distribution[i] = required[i]
            n -= required[i]
    
    return distribution

# Read input
n, m, s, d = map(int, input().split())
current = list(map(int, input().split()))

# Get the distribution of new bottles
result = refill_sodas(n, m, s, d, current)

# Output the result
if isinstance(result, list):
    print(" ".join(map(str, result)))
else:
    print(result)