MOD = 10**9 + 7

def power(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if (y & 1):
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res

def count_ways(k, n):
    if k == 1:
        return power(2, n, MOD) - 1
    
    ways = [0] * (n + 1)
    ways[0] = power(2, k, MOD) - 2
    for i in range(1, n + 1):
        ways[i] = (power(2, k * i, MOD) - 2 * ways[i-1] - ways[i-k]) % MOD
    
    return (ways[n] + MOD) % MOD

k, n = map(int, input().split())
print(count_ways(k, n))