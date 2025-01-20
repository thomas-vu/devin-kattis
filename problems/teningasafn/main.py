MOD = 10**9 + 7

def mod_pow(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

def sum_of_powers(n, k):
    total = 0
    for i in range(1, n + 1):
        total = (total + mod_pow(i, k, MOD)) % MOD
    return total

def main():
    n, k = map(int, input().split())
    result = sum_of_powers(n, k)
    print(result)

if __name__ == "__main__":
    main()