import sys
from math import log2, floor
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
c = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    s, t = map(int, input().split())
    graph[s].append(t)

dp = [[0] * (n + 1) for _ in range(n)]
satisfactions = [0] * n

def dfs(node, visited):
    if visited[node]:
        return dp[node][visited.count(True)]
    visited[node] = True
    max_sat = 0
    for neighbor in graph[node]:
        if not visited[neighbor]:
            max_sat = max(max_sat, dfs(neighbor, visited))
    dp[node][visited.count(True)] = max_sat + c[node] / (2 ** visited.count(True))
    visited[node] = False
    return dp[node][visited.count(True)]

max_satisfaction = 0
for i in range(n):
    visited = [False] * n
    max_satisfaction = max(max_satisfaction, dfs(i, visited))

print("{:.6f}".format(max_satisfaction))