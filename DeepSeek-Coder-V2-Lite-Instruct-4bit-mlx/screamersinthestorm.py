MOD = 10**9 + 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def count_configurations(K, N):
    if K == 1:
        return pow(2, N - 1, MOD)
    
    dp = [[0] * (N + 1) for _ in range(K + 1)]
    dp[1][1] = 1
    
    for i in range(2, K + 1):
        for j in range(1, N + 1):
            if i == j:
                dp[i][j] = pow(2, j - 1, MOD)
            else:
                for k in range(1, i):
                    if gcd(i, k) == 1:
                        dp[i][j] = (dp[i][j] + dp[k][j - 1]) % MOD
    
    result = sum(dp[i][N] for i in range(1, K + 1)) % MOD
    return result

K, N = map(int, input().split())
print(count_configurations(K, N))