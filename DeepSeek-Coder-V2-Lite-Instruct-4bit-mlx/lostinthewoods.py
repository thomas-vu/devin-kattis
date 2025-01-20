import sys
from math import factorial

# Read input
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    K, L = map(int, sys.stdin.readline().split())
    graph[K].append(L)
    graph[L].append(K)

# Calculate expected time using dynamic programming with probabilities
dp = [[0.0] * N for _ in range(1 << N)]
dp[(1 << N) - 1][0] = 1.0
for state in range(1 << N - 1, -1, -1):
    for v in range(N):
        if state & (1 << v):
            for nv in graph[v]:
                if not (state & (1 << nv)):
                    dp[state][v] += dp[state | (1 << nv)][nv] / len(graph[nv])
dp = [[dp[state][v] / factorial(bin(state).count('1') - 1) if bin(state).count('1') > 1 else 0.0 for v in range(N)] for state in range(1 << N)]

# Calculate the expected time to reach the exit
expected_time = 0.0
for state in range(1 << N):
    for v in range(N):
        if state & (1 << v):
            expected_time += dp[state][v] * bin(state).count('1')
print("{:.5f}".format(expected_time))