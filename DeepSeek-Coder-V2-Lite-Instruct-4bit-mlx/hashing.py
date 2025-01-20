import sys

# Read the input string and number of queries
S = sys.stdin.readline().strip()
Q = int(sys.stdin.readline())
queries = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(Q)]

# Define constants for the polynomial rolling hash function
BASE = 29
MOD = 10**9 + 7

# Precompute the powers of BASE modulo MOD
power = [1]
for _ in range(len(S)):
    power.append((power[-1] * BASE) % MOD)

# Precompute the hash for all substrings using dynamic programming
dp = [[0] * (len(S) + 1) for _ in range(26)]
for i in range(len(S)):
    char_index = ord(S[i]) - ord('a')
    for j in range(26):
        dp[j][i + 1] = (dp[j][i] * BASE) % MOD
    dp[char_index][i + 1] = (dp[char_index][i] + power[i]) % MOD

# Function to compute the hash of a substring [L, R)
def hash_substring(L, R):
    result = 0
    for j in range(26):
        h = (dp[j][R] - dp[j][L] * power[R - L]) % MOD
        if h < 0:
            h += MOD
        result ^= h
    return result

# Process each query and output the hash
for L, R in queries:
    print(hash_substring(L, R))