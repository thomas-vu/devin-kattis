import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while not is_prime(n):
        n += 1
    return n

while True:
    n = int(input())
    if n == 0:
        break
    print(next_prime(2 * n) if is_prime(n) else f"{next_prime(2 * n)} ({n} is not prime)")