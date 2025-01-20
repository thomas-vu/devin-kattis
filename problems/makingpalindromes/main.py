MOD = 10**9 + 7

def count_palindromic_subsequences(N, S):
    # Initialize the DP table with 0s
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Base case: single character palindromes
    for i in range(N):
        dp[i + 1][i] = 1
    
    # Fill the DP table
    for length in range(2, N + 1):
        for start in range(N - length + 2):
            end = start + length - 1
            if S[start] == S[end]:
                dp[start][end] = (dp[start + 1][end - 1] * 2) % MOD
            else:
                dp[start][end] = (dp[start + 1][end - 1]) % MOD
            dp[start][end] = (dp[start][end] + dp[start][end - 1]) % MOD
            dp[start][end] = (dp[start][end] + dp[start + 1][end]) % MOD
    
    # The result is the sum of all palindromic subsequences ending at each position
    result = 0
    for i in range(N):
        result = (result + dp[i][i]) % MOD
    
    return result

# Read input
N = int(input().strip())
S = input().strip()

# Output the result
print(count_palindromic_subsequences(N, S))