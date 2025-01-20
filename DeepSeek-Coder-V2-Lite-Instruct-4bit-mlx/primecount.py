import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes(N):
    if N < 2:
        return 0
    primes = [True] * (N + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(N)) + 1):
        if primes[i]:
            for j in range(i * i, N + 1, i):
                primes[j] = False
    return sum(primes)

N = int(input())
print(count_primes(N))