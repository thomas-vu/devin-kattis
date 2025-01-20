def count_ways(M, N, times):
    dp = [0] * (M + 1)
    dp[0] = 1
    
    for time in times:
        for j in range(M - time + 1):
            if dp[j]:
                dp[j + time] += dp[j]
    
    return dp[M]

def main():
    M = int(input().strip())
    N = int(input().strip())
    times = [int(input().strip()) for _ in range(N)]
    result = count_ways(M, N, times)
    print(result)

if __name__ == "__main__":
    main()