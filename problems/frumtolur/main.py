def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(num):
    primes = []
    candidate = 2
    while len(primes) < num:
        if is_prime(candidate):
            primes.append(candidate)
        candidate += 1
    return primes

primes = generate_primes(100)
for prime in primes:
    print(prime)