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

def solve(n, t, operations):
    mod = n
    for op, x, y in operations:
        if op == '+':
            print((x + y) % mod)
        elif op == '-':
            print((x - y) % mod)
        elif op == '*':
            print((x * y) % mod)
        elif op == '/':
            if y == 0:
                print(-1)
            else:
                try:
                    inv_y = modinv(y, n)
                    print((x * inv_y) % mod)
                except Exception:
                    print(-1)

while True:
    line = input()
    if line == '0 0':
        break
    n, t = map(int, line.split())
    operations = []
    for _ in range(t):
        op, x, y = input().split()
        x, y = int(x), int(y)
        operations.append((op, x, y))
    solve(n, t, operations)