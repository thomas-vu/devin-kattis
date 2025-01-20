import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(N):
    for i in range(2, N - 2 + 1):
        if is_prime(i) and is_prime(N - i - 2):
            return [i, N - i - 2, 2]
    return "Neibb"

# Read input
N = int(input())

# Check for violation of Goldbach's second conjecture
if N % 2 == 0:
    print("Neibb")
else:
    primes = find_primes(N)
    if primes == "Neibb":
        print("Neibb")
    else:
        primes.sort()
        print(f"{primes[0]} {primes[1]} {primes[2]}")