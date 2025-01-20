def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def solve(a, n, b, m):
    K = n * m // extended_gcd(n, m)[0]
    x = (a + n * modinv(n, m) * (b - a)) % K
    return x, K

def main():
    T = int(input())
    for _ in range(T):
        a, n, b, m = map(int, input().split())
        try:
            x, K = solve(a, n, b, m)
            print(x, K)
        except Exception:
            print("no solution")

if __name__ == "__main__":
    main()