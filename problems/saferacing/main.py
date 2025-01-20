MOD = 123456789

def count_ways(L, S):
    if L < S:
        return 0
    
    ways = [0] * (L + 1)
    ways[0] = 1
    
    for i in range(S, L + 1):
        ways[i] = (ways[i - 1] + ways[i - S]) % MOD
        if i > S:
            ways[i] = (ways[i] + ways[i - 1]) % MOD
    
    return ways[L]

# Read input
L, S = map(int, input().split())
W = count_ways(L, S)
print(W)