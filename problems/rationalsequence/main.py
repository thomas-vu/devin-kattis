def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lowest_terms(p, q):
    g = gcd(p, q)
    return p // g, q // g

def find_next(p, q):
    if p == 1 and q == 1:
        return (2, 1)
    if p == 1 or q == 1:
        return (1, 1)
    if p > q:
        new_p = p - q
        new_q = q
    else:
        new_p = p
        new_q = q - p
    return lowest_terms(new_p, new_q)

P = int(input())
for _ in range(P):
    K, p, q = map(int, input().split())
    next_p, next_q = find_next(p, q)
    print(f"{K} {next_p}/{next_q}")