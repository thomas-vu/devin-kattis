MOD = 10**9 + 7

def prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def S(X):
    factors = prime_factors(X)
    return sum(factors)

def find_min_max(N):
    min_x = float('inf')
    max_x = 0
    
    for i in range(1, N + 1):
        if S(i) == N:
            min_x = min(min_x, i)
            max_x = max(max_x, i)
    
    return min_x, max_x

# Given N
N = int(input())
min_x, max_x = find_min_max(N)
print(min_x % MOD, max_x % MOD)