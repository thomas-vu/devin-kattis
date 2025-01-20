import math
from scipy.special import comb, factorial

def calculate_probability(P, distribution):
    total = sum(distribution)
    n = len(distribution)
    ways_to_distribute = comb(P, sum(distribution), exact=False)
    ways_to_arrange = factorial(sum(distribution))
    for count in distribution:
        ways_to_arrange //= factorial(count)
    probability = ways_to_distribute * ways_to_arrange / (365 ** P)
    return math.log10(probability)

# Read input
n = int(input())
distribution = list(map(int, input().split()))

# Calculate and print the result
result = calculate_probability(n, distribution)
print("{:.12f}".format(result))