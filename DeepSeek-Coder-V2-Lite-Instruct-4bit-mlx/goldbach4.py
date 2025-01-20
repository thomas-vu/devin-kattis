import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(N):
    for i in range(2, N - 1):
        if is_prime(i) and is_prime(N - i - 2):
            return [i, 2, N - i - 2]
    return "Neibb"

# Read input
N = int(input())

# Find and print the primes
primes = find_primes(N)
if primes == "Neibb":
    print("Neibb")
else:
    print(*primes)