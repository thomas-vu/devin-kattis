MOD = 10**9 + 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def count_sequences(P, N, M):
    G = [int(x) for x in input().split()]
    L = [int(x) for x in input().split()]
    
    # Initialize the result to 1, since each xi must be a multiple of Gi
    result = 1
    
    for i in range(N):
        count_g = 0
        for mask in range(1 << M):
            prod_lcm = 1
            count_l = 0
            for j in range(M):
                if mask & (1 << j):
                    prod_lcm = lcm(prod_lcm, L[j])
                    count_l += 1
            if count_l % G[i] == 0:
                count_g += 1
        result = (result * count_g) % MOD
    
    return result

P, N, M = map(int, input().split())
print(count_sequences(P, N, M))