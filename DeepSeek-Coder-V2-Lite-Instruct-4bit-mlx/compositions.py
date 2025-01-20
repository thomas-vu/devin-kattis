def count_compositions(n, m, k):
    # Using dynamic programming to count the number of compositions missing the sequence {m + i * k}
    dp = [1] + [0] * n
    for _ in range(n):
        new_dp = dp[:]
        for i in range(m, n + 1, k):
            for j in range(i, n + 1):
                new_dp[j] += dp[j - i]
        dp = new_dp
    return dp[n]

def main():
    P = int(input())
    results = []
    for _ in range(P):
        K, n, m, k = map(int, input().split())
        result = count_compositions(n, m, k)
        results.append((K, result))
    
    for K, result in results:
        print(f"{K} {result}")

if __name__ == "__main__":
    main()