MOD = 1001113

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = (result * i) % MOD
    return result

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

def nCrModp(n, r, p):
    if (r == 0):
        return 1
    numerator = factorial(n)
    denominator = (factorial(r) * factorial(n - r)) % p
    return (numerator * modInverse(denominator, p) % p) % p

def PDC(N, v):
    if v == 0:
        return factorial(N)
    elif v == N - 1:
        return factorial(N)
    else:
        result = (nCrModp(N - 1, v, MOD) * factorial(v + 1) * factorial(N - v - 1)) % MOD
        return result

def main():
    P = int(input())
    for _ in range(P):
        K, N, v = map(int, input().split())
        result = PDC(N, v)
        print(f"{K} {result}")

if __name__ == "__main__":
    main()