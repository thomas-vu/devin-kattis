MOD = 10**9 + 7

def factorial_mod(n, mod):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % mod
    return fact

def inverse_factorial_mod(n, mod):
    fact = factorial_mod(n, mod)
    inv_fact = [1] * (n + 1)
    inv_fact[n] = pow(fact[n], mod - 2, mod)
    for i in range(n - 1, 0, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % mod
    return inv_fact

def nCr_mod(n, r, fact, inv_fact, mod):
    if r > n:
        return 0
    return (fact[n] * inv_fact[r] % mod) * inv_fact[n - r] % mod

def count_paths(N, X, Y):
    fact = factorial_mod(N, MOD)
    inv_fact = inverse_factorial_mod(N, MOD)
    
    def count_valid_hops(start, end):
        x1, y1 = start
        x2, y2 = end
        count = 0
        while x1 < x2 and y1 < y2:
            count += 1
            x1 += X
            y1 += Y
        return count
    
    paths = 1
    for x in range(X, N + 1, X):
        for y in range(Y, N + 1, Y):
            if x == X and y == Y:
                continue
            paths *= nCr_mod(count_valid_hops((0, 0), (x, y)), paths, fact, inv_fact, MOD)
            paths %= MOD
    
    return paths

# Read input
N, X, Y = map(int, input().split())
print(count_paths(N, X, Y))