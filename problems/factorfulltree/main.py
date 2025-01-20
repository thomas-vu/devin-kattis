import sys
from math import gcd

def find_lcm(a, b):
    return a * b // gcd(a, b)

def dfs(v, p):
    if v == 1:
        x[v] = 1
    else:
        x[v] = find_lcm(x[p], edges[p].pop())
    for u in tree[v]:
        if u != p:
            dfs(u, v)

N = int(input())
tree = [[] for _ in range(N + 1)]
edges = {}
for _ in range(N - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
    edges[(u, v)] = 1

x = [0] * (N + 1)
dfs(1, -1)
print(' '.join(map(str, x[1:])))