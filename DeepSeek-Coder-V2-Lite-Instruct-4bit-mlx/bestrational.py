def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def best_rational_approximation(K, M, x):
    best_num = 0
    best_denom = 1
    min_diff = float('inf')
    
    for q in range(1, M + 1):
        p = int(x * q)
        if gcd(p, q) == 1:
            diff = abs(x - p / q)
            if diff < min_diff:
                min_diff = diff
                best_num = p
                best_denom = q
    
    return f"{K} {best_num}/{best_denom}"

P = int(input())
for _ in range(P):
    K, M, x = input().split()
    M = int(M)
    x = float(x)
    print(best_rational_approximation(K, M, x))