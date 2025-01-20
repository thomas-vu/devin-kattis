from math import gcd
from fractions import Fraction

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_probability(number):
    base = 0
    if number.startswith('0b'):
        base = 2
        number = number[2:]
    elif number.startswith('0o'):
        base = 8
        number = number[2:]
    elif number.startswith('0'):
        base = 8
        number = number[1:]
    else:
        base = 10
    
    decimal_number = int(number, base)
    return Fraction(is_prime(decimal_number), 1) if is_prime(decimal_number) else Fraction(0, 1)

def main():
    T = int(input())
    results = []
    for _ in range(T):
        number = input().strip()
        results.append(calculate_probability(number))
    
    for result in results:
        print(f"{result.numerator}/{result.denominator}")

if __name__ == "__main__":
    main()