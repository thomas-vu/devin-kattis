import sys
from math import gcd

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m if x1 < 0 else x1

def main():
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, e = map(int, sys.stdin.readline().strip().split())
        p = 1
        q = n // p
        while gcd(p, q) != 1:
            p += 1
            q = n // p
        phi_n = (p - 1) * (q - 1)
        d = modinv(e, phi_n)
        print(d)

if __name__ == "__main__":
    main()