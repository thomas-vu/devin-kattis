import sys
from math import gcd

def prime_factors(n):
    factors = []
    # Count the number of 2s that divide n
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # n must be odd at this point, so a skip of 2 (i = i + 2) can be used
    for i in range(3, int(n**0.5) + 1, 2):
        # While i divides n, append i and divide n
        while n % i == 0:
            factors.append(i)
            n //= i
    # If n is a prime number greater than 2, then it will not become 1 by above two steps
    if n > 2:
        factors.append(n)
    return factors

def find_divisors(factors):
    if not factors:
        yield 1
        return
    first, rest = factors[0], factors[1:]
    count = factors.count(first)
    for i in range(count + 1):
        combination = [first**i]
        for subset in find_divisors(rest):
            yield combination[0] * subset

def main():
    N = int(sys.stdin.readline().strip())
    divisors = list(map(int, sys.stdin.readline().strip().split()))
    
    # Count the frequency of each divisor
    freq = {}
    for div in divisors:
        freq[div] = freq.get(div, 0) + 1
    
    # Find the prime factors and their powers
    factors = []
    for div, cnt in freq.items():
        factors.append((div, cnt))
    
    # Generate all divisors from prime factors and their powers
    min_divisor = float('inf')
    for divs in find_divisors(factors):
        min_divisor = min(min_divisor, divs)
    
    # Find the other divisor by multiplying with min_divisor and N/min_divisor
    A = min(min_divisor, divisors[0] // min_divisor)
    B = A * (min_divisor if min_divisor != divisors[0] // min_divisor else N//min_divisor)
    
    print(A, B)

if __name__ == "__main__":
    main()