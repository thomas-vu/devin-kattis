def count_words(N, K, M):
    MOD = 2**M
    
    # Initialize a DP array where dp[i][j] represents the number of ways to get hash j for word length i
    dp = [[0] * MOD for _ in range(N + 1)]
    dp[0][0] = 1  # Base case: empty word has hash 0
    
    for length in range(1, N + 1):
        for letter_ord in range(1, 27):
            for prev_hash in range(MOD):
                new_hash = ((prev_hash * 33) ^ letter_ord) % MOD
                if new_hash == K:
                    dp[length][new_hash] += dp[length - 1][prev_hash]
    
    # The result is the number of ways to get hash K for a word of length N
    return dp[N][K]

# Read input values
import sys
input = sys.stdin.read
N, K, M = map(int, input().split())

# Calculate and print the result
result = count_words(N, K, M)
print(result)