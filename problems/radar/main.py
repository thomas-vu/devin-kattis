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

def crt(m, x, y):
    M = 1
    for mi in m:
        M *= mi
    
    Mi = [M // mi for mi in m]
    ti = [modinv(Mi[i], m[i]) for i in range(len(m))]
    
    z = 0
    for i in range(len(m)):
        z += x[i] * Mi[i] * ti[i]
    
    return z % M

m = list(map(int, input().split()))
x = list(map(int, input().split()))
y = list(map(int, input().split()))

print(crt(m, x, y))