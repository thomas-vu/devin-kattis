import itertools
from math import prod

def calculate_max_min_distinct_and_expected(weights):
    min_weight = float('inf')
    max_weight = 0
    distinct_weights = set()
    total_combinations = list(itertools.combinations(weights, 4))
    
    for combo in total_combinations:
        current_weight = sum(combo)
        min_weight = min(min_weight, current_weight)
        max_weight = max(max_weight, current_weight)
        distinct_weights.add(current_weight)
    
    expected_weight = sum([sum(combo) for combo in total_combinations]) / len(total_combinations)
    
    return max_weight, min_weight, len(distinct_weights), expected_weight

# Read input
N = int(input())
weights = list(map(int, input().split()))

# Calculate the required values
max_weight, min_weight, distinct_weights, expected_weight = calculate_max_min_distinct_and_expected(weights)

# Output the results
print(max_weight, min_weight, distinct_weights, f"{expected_weight:.5f}")