from math import comb
import sys

# Function to calculate the number of divisors of a given number
def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    return divisors

# Read from stdin
for line in sys.stdin:
    n, k = map(int, line.split())
    # Use the comb function to calculate binomial coefficient
    n_choose_k = comb(n, k)
    # Output the number of divisors of n choose k
    print(count_divisors(n_choose_k))