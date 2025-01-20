def expected_points(n, k, probabilities):
    dp = [[0.0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1.0
    
    for i in range(1, n + 1):
        pi = probabilities[i - 1]
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j] * (1.0 - pi)
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1] * pi
    
    expected_value = sum(dp[n][k:]) / (1.0 - (sum(probabilities) - sum(probabilities[:k])))
    return expected_value

def main():
    n, k = map(int, input().split())
    probabilities = list(map(float, input().split()))
    result = expected_points(n, k, probabilities)
    print("{:.10f}".format(result))

if __name__ == "__main__":
    main()