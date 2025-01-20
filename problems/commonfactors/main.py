from math import gcd
from fractions import Fraction

def f(n):
    count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            while n % i == 0:
                n //= i
    if n > 1:
        count += 1
    return count

def g(n):
    num_common_factors = f(n)
    return Fraction(num_common_factors, n)

def main():
    n = int(input())
    result = g(n)
    print(result.numerator, '/', result.denominator, sep='')

if __name__ == "__main__":
    main()