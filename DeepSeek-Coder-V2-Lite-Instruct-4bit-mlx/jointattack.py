# Solution in Python 3
import math

def continued_fraction_to_fraction(coefficients):
    if len(coefficients) == 1:
        return coefficients[0], 1
    
    num, denom = coefficients[-1], 1
    for i in range(len(coefficients) - 2, -1, -1):
        num, denom = coefficients[i] * num + denom, num
    
    gcd = math.gcd(num, denom)
    return num // gcd, denom // gcd

# Read input
n = int(input())
coefficients = list(map(int, input().split()))

# Convert to fraction and output the result
numerator, denominator = continued_fraction_to_fraction(coefficients)
print(f"{numerator}/{denominator}")