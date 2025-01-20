MOD = 1_000_000_007

def read_ints():
    return list(map(int, input().split()))

# Read the automaton description
n, c, s, f = read_ints()
alphabet = input().strip()
final_states = set(read_ints())
transitions = [list(read_ints()) for _ in range(n)]

# Initialize the DP table
dp = [[0] * n for _ in range(5001)]
dp[0][s - 1] = 1

# Compute the DP table for each length up to the maximum query length
for l in range(1, 5001):
    for state in range(n):
        for symbol_idx, symbol in enumerate(alphabet):
            next_state = transitions[state][symbol_idx] - 1
            dp[l][next_state] = (dp[l][next_state] + dp[l - 1][state]) % MOD

# Process the queries
m = int(input())
for _ in range(m):
    query_len = int(input())
    result = 0
    for final_state in final_states:
        result = (result + dp[query_len][final_state - 1]) % MOD
    print(result)