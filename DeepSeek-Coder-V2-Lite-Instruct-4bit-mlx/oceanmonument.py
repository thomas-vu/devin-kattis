def count_optimal_orders(g, e):
    if g == 0:
        return 1
    if e == 0:
        return 1
    dp = [[0] * (e + 1) for _ in range(g + 1)]
    dp[0][0] = 1
    
    for i in range(g + 1):
        for j in range(e + 1):
            if i > 0 and j < e:
                dp[i][j] += dp[i - 1][j + 1]
            if j > 0:
                dp[i][j] += dp[i][j - 1]
    
    return dp[g][e]

def main():
    t = int(input())
    for _ in range(t):
        g, e = map(int, input().split())
        print(count_optimal_orders(g, e))

if __name__ == "__main__":
    main()