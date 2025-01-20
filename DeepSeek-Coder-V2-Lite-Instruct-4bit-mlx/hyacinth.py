def read_ints():
    return list(map(int, input().split()))

n = int(input())
edges = [read_ints() for _ in range(n - 1)]
graph = {i: [] for i in range(1, n + 1)}
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

freq = [0] * (2 * n)
visited = [False] * (2 * n)

def dfs(node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            freq[neighbor] = (freq[node] + 1) % 10**9
            dfs(neighbor)

dfs(1)
for i in range(1, n + 1):
    print(freq[i], freq[i + n])