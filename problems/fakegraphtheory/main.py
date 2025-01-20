MOD = 1_000_003_233

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result = (result * i) % MOD
    return result

def pow_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def inverse_factorial(n):
    fact = factorial(n)
    return pow_mod(fact, MOD - 2, MOD)

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return (factorial(n) * inverse_factorial(r) * inverse_factorial(n - r)) % MOD

def main():
    n = int(input())
    fact_4n = factorial(4 * n)
    inv_fact_2n = inverse_factorial(2 * n)
    E = (pow_mod(4, n, MOD) - 2 * pow_mod(3, n, MOD) + pow_mod(2, n, MOD)) * inv_fact_2n % MOD
    E = (E * factorial(2 * n)) % MOD
    print(E)

if __name__ == "__main__":
    main()