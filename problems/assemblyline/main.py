import sys

# Read input
k = int(sys.stdin.readline().strip())
symbols = sys.stdin.readline().strip().split()
assembly_table = [[0] * k for _ in range(k)]
for i in range(k):
    assembly_table[i] = [tuple(map(int, x.split('-')) if '-' in x else (int(x), x)) for x in sys.stdin.readline().strip().split()]
n = int(sys.stdin.readline().strip())
sequences = [sys.stdin.readline().strip() for _ in range(n)]

# Dynamic programming to find the minimum time and resulting symbol for each sequence
dp = [[float('inf')] * k for _ in range(k)]
result_symbols = [None] * k
for i, sym in enumerate(symbols):
    dp[i][i] = 0
    result_symbols[i] = sym

for length in range(2, k + 1):
    for i in range(k - length + 1):
        j = i + length - 1
        for k in range(i, j):
            for a in range(k):
                for b in range(a + 1, k):
                    time_ab = dp[i][k] + dp[k+1][j] + assembly_table[symbols.index(symbols[a])][symbols.index(symbols[b])][0]
                    time_ba = dp[i][k] + dp[k+1][j] + assembly_table[symbols.index(symbols[b])][symbols.index(symbols[a])][0]
                    if time_ab < dp[i][j]:
                        dp[i][j] = time_ab
                        symbols[a], symbols[b] = symbols[b], symbols[a]
                    if time_ba < dp[i][j]:
                        dp[i][j] = time_ba
                        symbols[a], symbols[b] = symbols[b], symbols[a]

# Output the results for each sequence
for seq in sequences:
    min_time = float('inf')
    final_symbol = None
    for i in range(k):
        for j in range(i + 1, k):
            time_seq = dp[0][i] + dp[i+1][j] + dp[j+1][k]
            if time_seq < min_time:
                min_time = time_seq
                final_symbol = symbols[j]
            elif time_seq == min_time and symbols.index(symbols[j]) < symbols.index(final_symbol):
                final_symbol = symbols[j]
    print(f"{min_time}-{final_symbol}")