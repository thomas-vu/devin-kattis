import math

def phi(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result

def is_primitive_root(g, m):
    order = phi(m)
    for k in range(1, order + 1):
        if pow(g, k, m) == 1:
            return k == order
    return False

def find_primitive_root(m):
    if m == 1:
        return 0
    elif m == 2 or m == 4:
        return 1 if m == 2 else 2
    prime_factors = set()
    n = phi(m)
    temp_n = n
    p = 2
    while p * p <= temp_n:
        if temp_n % p == 0:
            prime_factors.add(p)
            while temp_n % p == 0:
                temp_n //= p
        p += 1
    if temp_n > 1:
        prime_factors.add(temp_n)
    
    for g in range(1, m):
        if all(pow(g, k, m) != 1 for k in prime_factors):
            return g
    return -1

m = int(input())
print(find_primitive_root(m))