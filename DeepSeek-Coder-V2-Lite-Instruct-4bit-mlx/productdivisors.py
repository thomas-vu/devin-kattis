MOD = 10**9 + 7

def sieve(max_val):
    spf = list(range(max_val + 1))
    for i in range(2, int(max_val**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, max_val + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

def get_factors(x, spf):
    factors = {}
    while x != 1:
        p = spf[x]
        factors[p] = factors.get(p, 0) + 1
        x //= p
    return factors

def modinv(a, m):
    a = a % m
    x, y = 0, 1
    while a > 0:
        q = m // a
        (m, a), (x, y) = (a, m - q * a), (y, x - q * y)
    return x % m if b == 1 else x % m

n = int(input())
a = list(map(int, input().split()))
max_val = max(a)
spf = sieve(max_val)

product = 1
for num in a:
    product = (product * num) % MOD

factors = get_factors(product, spf)
num_divisors = 1
for count in factors.values():
    num_divisors *= (count + 1)
    num_divisors %= MOD

print(num_divisors)