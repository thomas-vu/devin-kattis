import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def max_prime_sum(N):
    primes = [i for i in range(2, N + 1) if is_prime(i)]
    max_terms = 0
    
    for i in range(len(primes)):
        sum_primes = 0
        for j in range(i, len(primes)):
            sum_primes += primes[j]
            if sum_primes == N:
                max_terms = max(max_terms, j - i + 1)
            elif sum_primes > N:
                break
    
    return max_terms

# Read input
N = int(input().strip())
print(max_prime_sum(N))