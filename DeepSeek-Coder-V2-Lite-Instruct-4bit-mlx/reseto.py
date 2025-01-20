def sieve_of_eratosthenes(N, K):
    is_prime = [True] * (N + 1)
    primes = []
    for p in range(2, N + 1):
        if is_prime[p]:
            primes.append(p)
            for multiple in range(p * p, N + 1, p):
                is_prime[multiple] = False
    return primes[K - 1]

# Input reading and function call
N, K = map(int, input().split())
print(sieve_of_eratosthenes(N, K))