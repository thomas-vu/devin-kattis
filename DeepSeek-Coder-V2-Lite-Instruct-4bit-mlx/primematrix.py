import sys
from math import sqrt

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Helper function to generate a prime matrix
def generate_prime_matrix(n, b):
    # Generate the first n*n prime numbers up to b+1 (since we need numbers between 1 and b)
    primes = [i for i in range(2, b + 1) if is_prime(i)]
    
    # Check if we have enough primes to fill the matrix
    if len(primes) < n * n:
        return "impossible"
    
    # Create the matrix with prime numbers up to b
    matrix = []
    for i in range(n):
        row = primes[i * n:(i + 1) * n]
        if not is_prime(sum(row)):
            return "impossible"
        matrix.append(row)
    
    # Check the column sums
    for j in range(n):
        col_sum = sum([matrix[i][j] for i in range(n)])
        if not is_prime(col_sum):
            return "impossible"
    
    return matrix

# Read input
n, b = map(int, sys.stdin.readline().split())

# Generate and output the prime matrix
matrix = generate_prime_matrix(n, b)
if matrix == "impossible":
    print("impossible")
else:
    for row in matrix:
        print(' '.join(map(str, row)))