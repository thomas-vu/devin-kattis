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

def point_addition(x1, y1, x2, y2, a, p):
    if (x1, y1) == (-1, -1):
        return (x2, y2)
    if (x2, y2) == (-1, -1):
        return (x1, y1)
    if x1 == x2 and y1 != y2:
        return (-1, -1)
    if x1 == x2 and y1 == y2:
        lam = (3 * x1 * x1 + a) * modinv(2 * y1, p) % p
    else:
        lam = (y2 - y1) * modinv(x2 - x1, p) % p
    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p
    return (int(x3), int(y3))

def scalar_multiplication(n, x, y, a, p):
    result = (-1, -1)
    for i in range(64):
        if n & (1 << i):
            result = point_addition(result[0], result[1], x, y, a, p)
        x, y = point_addition(x, y, x, y, a, p)
    return result

p = int(input())
a = int(input())
b = int(input())
n = int(input())
x_2 = int(input())
y_2 = int(input())

if x_2 == -1 and y_2 == -1:
    point = (-1, -1)
else:
    point = (x_2, y_2)

result = scalar_multiplication(n, point[0], point[1], a, p)
if result == (-1, -1):
    print("-1 -1")
else:
    print(f"{result[0]} {result[1]}")