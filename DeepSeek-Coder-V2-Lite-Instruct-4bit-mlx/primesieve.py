import sys
from math import sqrt, ceil

def is_prime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(n):
    prime_count = 0
    for i in range(1, n + 1):
        if is_prime(i):
            prime_count += 1
    return prime_count

# Read input
n, q = map(int, sys.stdin.readline().split())

# Output the number of primes less than or equal to n
print(count_primes(n))

# Process each query
for _ in range(q):
    x = int(sys.stdin.readline())
    print(1 if is_prime(x) else 0)