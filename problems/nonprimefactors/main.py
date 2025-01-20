Here's the complete solution in Python 3:

```python
import sys
from math import sqrt

# Fast I/O setup
input = sys.stdin.readline

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Precompute non-prime factors for all numbers up to 2*10^6
non_prime_factors = [0] * (2 * 10**6 + 1)
for i in range(2, int(sqrt(2 * 10**6)) + 1):
    if not is_prime(i):
        for j in range(i * i, 2 * 10**6 + 1, i):
            if not is_prime(j):
                non_prime_factors[j] += 1

# Read number of queries
Q = int(input())
for _ in range(Q):
    i = int(input())
    # Subtract the number of prime factors from total factors to get non-prime factors
    print(non_prime_factors[i])