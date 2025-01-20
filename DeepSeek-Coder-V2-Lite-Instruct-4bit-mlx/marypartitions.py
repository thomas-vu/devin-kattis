def count_m_ary_partitions(n, m):
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            dp[j] += dp[j - i]
    
    return dp[n]

def main():
    P = int(input())
    results = []
    
    for _ in range(P):
        K, m, n = map(int, input().split())
        result = count_m_ary_partitions(n, m)
        results.append((K, result))
    
    for K, result in results:
        print(f"{K} {result}")

if __name__ == "__main__":
    main()