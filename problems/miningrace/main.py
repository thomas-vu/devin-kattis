import math

def calculate_probability(n, b):
    # The number of steps Steve and Alex will take forward and down is n each.
    # To avoid collision, Alex must be b steps behind Steve at some point.
    # The probability that Alex is exactly b steps behind Steve after k moves (0 <= k < n)
    # is given by the binomial coefficient and the total number of possible sequences.
    
    if b > n:
        return 0.0
    
    # Calculate the total number of possible sequences for Steve and Alex
    total_sequences = math.comb(2 * n, n)
    
    # Calculate the number of sequences where Alex is exactly b steps behind Steve
    favorable_sequences = math.comb(2 * n, n) - math.comb(2 * (n - b), n)
    
    # The probability of collision is the number of favorable sequences divided by the total sequences
    probability_of_collision = (favorable_sequences / total_sequences) * 100
    
    return probability_of_collision

# Read input
n, b = map(int, input().split())

# Calculate and print the probability of collision
probability = calculate_probability(n, b)
print("{:.10f}".format(probability))