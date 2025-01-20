import sys
from itertools import combinations

def min_cost(n, d, prices):
    # Calculate the total cost of all items
    total_cost = sum(prices)
    
    # If there are no dividers, the cost is already minimized
    if d == 0:
        return total_cost
    
    # Calculate the cost of each possible group configuration
    min_cost = sys.maxsize
    for comb in combinations(prices, n - d):
        cost = sum(comb)
        rounded_cost = round_to_nearest_10(cost)
        min_cost = min(min_cost, rounded_cost)
    
    return min_cost

def round_to_nearest_10(x):
    remainder = x % 10
    if remainder < 5:
        return x - remainder
    else:
        return x + (10 - remainder)

# Read input
n, d = map(int, sys.stdin.readline().split())
prices = list(map(int, sys.stdin.readline().split()))

# Output the minimum cost
print(min_cost(n, d, prices))