import sys
from math import sqrt, log10

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Helper function to generate all possible primes of a given length
def generate_primes(length):
    if length == 0:
        return [""]
    sub_primes = generate_primes(length - 1)
    primes = []
    for digit in "2357":  # Only consider digits that are prime themselves
        for sub_prime in sub_primes:
            if is_prime(int(digit + sub_prime)):
                primes.append(digit + sub_prime)
    return primes

# Main function to count superprime grids
def count_superprime_grids(n, m):
    # Generate all possible primes for the given length of rows and columns
    row_primes = generate_primes(m)
    col_primes = generate_primes(n)
    
    # Count the number of superprime grids
    count = 0
    for row in row_primes:
        for col in col_primes:
            if is_prime(int(row + col)):
                count += 1
    return count

# Read input from stdin
n, m = map(int, sys.stdin.readline().strip().split())

# Output the result
print(count_superprime_grids(n, m))