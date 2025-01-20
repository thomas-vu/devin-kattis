import math
from collections import defaultdict

def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def max_revenue(N, S):
    factor_count = defaultdict(int)
    
    for s in S:
        factors = prime_factors(s)
        for factor in factors:
            factor_count[factor] += 1
    
    revenue = sum(factor_count.values())
    return revenue

# Read input
N = int(input().strip())
S = list(map(int, input().strip().split()))

# Calculate and print the maximum revenue
print(max_revenue(N, S))