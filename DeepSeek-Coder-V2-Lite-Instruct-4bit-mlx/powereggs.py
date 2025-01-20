def min_drops(N, K):
    if K == 1:
        return N
    elif K > 32:
        return "Impossible"
    
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    for i in range(1, N + 1):
        dp[i][1] = i
    
    for j in range(2, K + 1):
        for i in range(1, N + 1):
            dp[i][j] = float('inf')
            for x in range(1, i + 1):
                dp[i][j] = min(dp[i][j], max(dp[x - 1][j - 1], dp[i - x][j]) + 1)
    
    return dp[N][K]

def main():
    T = int(input())
    results = []
    for _ in range(T):
        N, K = map(int, input().split())
        results.append(min_drops(N, K))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()