import math
from collections import defaultdict

def prime_factors(n):
    factors = defaultdict(int)
    while n % 2 == 0:
        factors[2] += 1
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] += 1
            n //= i
    if n > 2:
        factors[n] += 1
    return factors

def largest_perfect_power(x):
    if x == 1:
        return 1
    
    factors = prime_factors(x)
    max_p = 1
    
    for base, exponent in factors.items():
        p = 1
        while exponent >= p:
            if base**p == x:
                max_p = max(max_p, p)
            exponent -= p
            p += 1
    
    return max_p

while True:
    x = int(input())
    if x == 0:
        break
    print(largest_perfect_power(x))