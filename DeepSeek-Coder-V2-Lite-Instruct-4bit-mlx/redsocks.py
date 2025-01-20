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

def solve(p, q):
    n = p * modinv(q, 2) % 2
    if n == 0:
        r = (p * modinv(q, 4)) % 2
        b = (1 - r) // 2
    else:
        return "impossible"
    
    if r < 0 or b < 0:
        return "impossible"
    
    return f"{int(r)} {int(b)}"

while True:
    line = input()
    if line == "0 0":
        break
    p, q = map(int, line.split())
    print(solve(p, q))