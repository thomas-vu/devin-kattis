MOD = 10**9 + 7

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def modInverse(n, p):
    return power(n, p - 2, p)

def modFact(n, p):
    if n >= p:
        return 0
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % p
    return modInverse(res, p)

def count_ways(n):
    total = 0
    for i in range(2, n + 1, 2):
        total = (total + (modFact(n, MOD) * modInverse(i, MOD) % MOD)) % MOD
    return total

n = int(input().strip())
print(count_ways(n))