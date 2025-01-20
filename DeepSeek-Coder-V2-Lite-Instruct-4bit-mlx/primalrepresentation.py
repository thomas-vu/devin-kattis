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

def format_factors(factors):
    factor_list = []
    for prime, count in factors.items():
        if count > 0:
            if count == 1:
                factor_list.append(str(prime))
            else:
                factor_list.append(f"{prime}^{count}")
    return " ".join(factor_list)

factors_cache = {}
while True:
    try:
        x = int(input())
        if x in factors_cache:
            print(factors_cache[x])
        else:
            if x < 0:
                print("-1", end=" ")
                x = -x
            factors = prime_factors(x)
            result = format_factors(factors)
            print(result)
            factors_cache[x] = result
    except EOFError:
        break