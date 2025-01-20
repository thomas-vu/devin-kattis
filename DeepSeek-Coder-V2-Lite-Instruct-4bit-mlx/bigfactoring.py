import math

def prime_factors(n):
    factors = []
    # Check for the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check for odd factors from 3 onwards
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    return factors

# Read the input
n = int(input())
factors = prime_factors(n)
# Print the factors in ascending order
for factor in sorted(set(factors)):
    count = factors.count(factor)
    print(factor, count)