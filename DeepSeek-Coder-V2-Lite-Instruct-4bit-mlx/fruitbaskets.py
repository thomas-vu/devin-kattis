def total_weight(N, weights):
    total = 0
    for weight in weights:
        if weight >= 200:
            total += weight
    return total

# Read input
N = int(input())
weights = list(map(int, input().split()))

# Calculate total weight of baskets with at least 200 grams of fruit
result = total_weight(N, weights)
print(result)