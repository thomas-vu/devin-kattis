def read_ints():
    return list(map(int, input().split()))

N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, X, T = read_ints()
    edges[A].append((B, X, T))

liquid_needed = read_ints()

# DFS to calculate the amount of liquid at each node
def dfs(node):
    if len(edges[node]) == 0:
        return liquid_needed[node - 1]
    
    total_liquid = 0.0
    for child, flow, is_super in edges[node]:
        child_liquid = dfs(child)
        if is_super:
            total_liquid += flow * child_liquid + (flow / 100) * child_liquid
        else:
            total_liquid += flow * child_liquid / 100
    return total_liquid

# Binary search to find the minimum amount of liquid needed
left, right = 0.1, 2 * 10**9
while abs(left - right) > 1e-6:
    mid = (left + right) / 2
    total_liquid = dfs(1, mid)
    if total_liquid < 2 * 10**9:
        left = mid
    else:
        right = mid
print("{:.3f}".format(left))