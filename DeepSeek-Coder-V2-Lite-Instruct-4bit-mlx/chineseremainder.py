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
    g = extended_gcd(n, m)[0]
    lcm = (n * m) // g
    n_inv = modinv(m, n)
    m_inv = modinv(n, m)
    x = (a + b + n * (m_inv * (b - a)) % m) % lcm
    return x, lcm

T = int(input())
for _ in range(T):
    a, n, b, m = map(int, input().split())
    x, K = solve(a, n, b, m)
    print(x, K)