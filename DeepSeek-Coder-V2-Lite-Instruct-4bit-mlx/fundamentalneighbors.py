import sys
from math import sqrt

def prime_factors(n):
    factors = {}
    # Check for number of 2s that divide n
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    # Check for odd factors from 3 onwards
    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    # If n is a prime number greater than 2
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors

def neighbor_number(factors):
    new_factorization = {}
    for prime, exponent in factors.items():
        new_factorization[exponent] = prime
    neighbor = 1
    for exponent, prime in new_factorization.items():
        neighbor *= prime**exponent
    return neighbor

for line in sys.stdin:
    n = int(line)
    factors = prime_factors(n)
    neighbor = neighbor_number(factors)
    print(f"{n} {neighbor}")