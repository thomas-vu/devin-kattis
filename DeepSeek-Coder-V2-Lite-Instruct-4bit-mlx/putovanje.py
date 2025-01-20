def max_fruits(N, C, weights):
    current_weight = 0
    distinct_fruits = 0
    for weight in weights:
        if current_weight + weight <= C:
            current_weight += weight
            distinct_fruits += 1
    return distinct_fruits

# Read input
N, C = map(int, input().split())
weights = list(map(int, input().split()))

# Output the result
print(max_fruits(N, C, weights))