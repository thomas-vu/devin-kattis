import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_prime_power(q):
    if q == 1:
        return True
    for k in range(2, int(math.sqrt(q)) + 1):
        if q % k == 0:
            p = q // k
            if is_prime(p) and (k == 1 or is_prime(k)):
                return True
    return False

q = int(input())
print("yes" if is_prime_power(q) else "no")