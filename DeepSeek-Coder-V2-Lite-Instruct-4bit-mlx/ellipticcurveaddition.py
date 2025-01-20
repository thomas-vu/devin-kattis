import sys

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m if g == 1 else None

def add_points(p, q, a, b, p_inf=False, q_inf=False):
    if p_inf:
        return q
    if q_inf:
        return p
    if p[0] == q[0]:
        if (p[1] + q[1]) % p_ == 0:
            return (-1, -1)
        lam = ((3 * p[0]**2 + a) * modinv((2 * p[1]), p_)) % p_
    else:
        lam = ((q[1] - p[1]) * modinv((q[0] - p[0]), p_)) % p_
    x3 = (lam**2 - p[0] - q[0]) % p_
    y3 = (lam * (p[0] - x3) - p[1]) % p_
    return (x3, y3)

# Read input
p = int(sys.stdin.readline().strip())
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
x1, y1 = map(int, sys.stdin.readline().strip().split())
x2, y2 = map(int, sys.stdin.readline().strip().split())

# Define points
P = (x1, y1)
Q = (x2, y2)

# Calculate P + Q
result = add_points(P, Q, a, b)

# Output result
if result == (-1, -1):
    print(-1, -1)
else:
    print(result[0], result[1])