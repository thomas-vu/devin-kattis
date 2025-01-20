import math

def calculate_probability(n, p):
    # Calculate the probability using the binomial distribution formula
    total_ways = math.comb(n + p, p)  # Total ways to choose p names from n+p
    bad_ways = math.comb(n, p)  # Ways to choose p names from n (cheating ways)
    good_ways = total_ways - bad_ways  # Good ways to choose p names with your name exactly once
    
    probability = good_ways / total_ways
    return probability

# Read input from stdin
n, p = map(int, input().split())

# Calculate and output the result
probability = calculate_probability(n, p)
print("{:.6f}".format(probability))