def count_subsequence(s, subseq):
    n = len(s)
    m = len(subseq)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == subseq[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 10000
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][m]

def main():
    T = int(input())
    for case_num in range(1, T + 1):
        text = input()
        result = count_subsequence(text, "welcome to code jam")
        print("Case #{}: {:04d}".format(case_num, result))

if __name__ == "__main__":
    main()