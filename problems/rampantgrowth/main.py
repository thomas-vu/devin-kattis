MOD = 998244353
def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f = (f * i) % MOD
    return f
def powmod(x, y):
    res = 1
    x = x % MOD
    while y > 0:
        if (y & 1):
            res = (res * x) % MOD
        y = y >> 1
        x = (x * x) % MOD
    return res
def inv(n):
    return powmod(n, MOD - 2)
def nCr_mod(n, r):
    if (r > n or n < 0 or r < 0):
        return 0
    num = factorial(n)
    den = (factorial(r) * factorial(n - r)) % MOD
    return (num * inv(den)) % MOD
r, c = map(int, input().split())
ans = (nCr_mod(r + c - 2, r - 1) * powmod(nCr_mod(r, c), MOD - 2)) % MOD
print(ans)