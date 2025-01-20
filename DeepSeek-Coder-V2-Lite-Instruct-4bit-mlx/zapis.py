def count_bracket_sequences(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(n + 1):
            if s[i] == '(':
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % 100000
            elif s[i] == ')':
                if j > 0:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % 100000
            elif s[i] == '?':
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % 100000
                if j > 0:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % 100000
            else:
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % 100000
    
    return dp[n][0]

# Read input
N = int(input())
s = input().strip()

# Calculate and output the result
result = count_bracket_sequences(s)
print(result)