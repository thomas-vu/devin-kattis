MOD = 10**9 + 7

def count_palindromic_subsequences(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the dp array
    for i in range(n):
        dp[i][i] = 1
    
    # Fill the dp array
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % MOD
            else:
                dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1] + MOD) % MOD
    
    return dp[0][n - 1]

def main():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        result = count_palindromic_subsequences(s)
        print(result)

if __name__ == "__main__":
    main()