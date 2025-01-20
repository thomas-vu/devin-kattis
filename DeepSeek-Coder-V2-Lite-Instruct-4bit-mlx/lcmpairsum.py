MOD = 10**9 + 7

def mod_pow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def f(n):
    factors = []
    original_n = n
    for i in range(2, int(original_n**0.5) + 1):
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors.append((i, count))
    if n > 1:
        factors.append((n, 1))
    
    result = 0
    for mask in range(1, 1 << len(factors)):
        lcm = 1
        sum_pairs = 0
        for i in range(len(factors)):
            if (mask & (1 << i)):
                lcm *= factors[i][0] ** factors[i][1]
        for p in range(1, lcm + 1):
            if lcm % p == 0:
                q = lcm // p
                sum_pairs += (p + q)
        result += sum_pairs * (pow(2, bin(mask).count('1') - 1, MOD) if bin(mask).count('1') % 2 == 1 else pow(-1, bin(mask).count('1'), MOD) * pow(2, bin(mask).count('1') - 1, MOD))
        result %= MOD
    return result

def main():
    T = int(input())
    for t in range(1, T + 1):
        C = int(input())
        factors = []
        for _ in range(C):
            P, a = map(int, input().split())
            factors.append((P, a))
        n = 1
        for P, a in factors:
            n *= P**a
        print(f"Case {t}: {f(n)}")

if __name__ == "__main__":
    main()