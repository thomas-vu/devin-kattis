import math

def smallest_n(phi):
    if phi == 1:
        return 2
    for i in range(2, int(math.sqrt(phi)) + 1):
        if phi % i == 0:
            n = (i - 1) * (phi // i)
            if is_coprime(n, phi):
                return n
    for p in prime_factors(phi):
        if is_coprime(p - 1, phi // p):
            return (p - 1) * (phi // (p - 1))
    return -1

def is_coprime(a, b):
    while b:
        a, b = b, a % b
    return a == 1

def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 2:
        factors.append(n)
    return factors

# Read the input value of phi
phi = int(input().strip())
print(smallest_n(phi))