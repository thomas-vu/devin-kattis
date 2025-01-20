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

def count_factor_permutations(factors):
    result = 1
    for exponent in factors.values():
        result *= (exponent + 1)
    return result

def smallest_k(n):
    factors = prime_factors(n)
    k = 1
    for factor, exponent in factors.items():
        k *= factor ** exponent
    return k

def main():
    while True:
        try:
            n = int(input())
            k = smallest_k(n)
            print(f"{n} {k}")
        except EOFError:
            break

if __name__ == "__main__":
    main()