Here's the complete solution in Python 3 that solves the given problem:

```python
import math

def prime_factors(n):
    factors = {}
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n //= i
    if n > 2:
        factors[n] = factors.get(n, 0) + 1
    return factors

def smallest_value(x):
    if x == 1:
        return 1
    
    factors = prime_factors(x)
    min_n = math.inf
    
    for p, k in factors.items():
        f_p = sum([math.ceil(i / p) for i in range(1, k + 1)])
        n = p ** f_p
        min_n = min(min_n, n)
    
    return min_n if min_n != math.inf else -1

# Read the input x
x = int(input().strip())
print(smallest_value(x))