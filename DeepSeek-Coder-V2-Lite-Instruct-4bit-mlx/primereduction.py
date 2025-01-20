def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def prime_reduction(x):
    count = 0
    while not is_prime(x):
        factors = prime_factors(x)
        x = sum(factors)
        count += 1
    return x, count

while True:
    line = input()
    if line == '4':
        break
    x = int(line)
    result, count = prime_reduction(x)
    print(result, count)