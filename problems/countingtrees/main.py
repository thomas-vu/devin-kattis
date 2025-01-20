MOD = 10**10 + 3233

def mod_pow(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def count_colorings(n, k, c):
    if n % (k * c) != 0:
        return 0
    
    total_nodes = n // c
    ways = mod_pow(k * c, total_nodes, MOD) - 1
    if ways < 0:
        ways += MOD
    
    inv = mod_pow(k * c - 1, MOD - 2, MOD)
    ways = (ways * inv) % MOD
    
    return ways

def main():
    C = int(input())
    results = []
    for _ in range(C):
        n, k, c = map(int, input().split())
        results.append(count_colorings(n, k, c))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()