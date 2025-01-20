from math import gcd

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

def discrete_log(P, B, N):
    if gcd(B, P) != 1:
        return "no solution"
    
    m = int(P ** 0.5) + 1
    table = {}
    
    # Baby-step giant-step algorithm
    for i in range(m):
        table[pow(B, i, P)] = i
    
    b_inv = modinv(pow(B, m, P), P)
    
    for i in range(m):
        y = (N * pow(b_inv, i, P)) % P
        if y in table:
            return (i * m + table[y]) % (P - 1)
    
    return "no solution"

while True:
    try:
        line = input().strip()
        if not line:
            break
        P, B, N = map(int, line.split())
        result = discrete_log(P, B, N)
        print(result)
    except EOFError:
        break