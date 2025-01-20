def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_even_primes(a, b):
    even_primes = []
    for num in range(a, b + 1):
        if is_prime(num) and num % 2 == 0:
            even_primes.append(num)
    return even_primes

a = int(input())
b = int(input())

even_primes = generate_even_primes(a, b)
if not even_primes:
    print(":(", end="")
else:
    print(len(even_primes))
    for prime in sorted(even_primes):
        print(prime, end=" ")