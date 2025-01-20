def dfs(node, graph, visited):
    if node in visited:
        return 0
    visited.add(node)
    count = 1 if node in gates else 0
    for neighbor in graph[node]:
        count += dfs(neighbor, graph, visited)
    visited.remove(node)
    return count

n = int(input())
m = int(input())
graph = {i: [] for i in range(n)}
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
k = int(input())
gates = set(map(int, input().split()))

visited = set()
winning_paths = dfs(0, graph, visited)
total_paths = sum(dfs(node, graph, set()) for node in range(n))

print("winning paths", winning_paths)
print("total paths", total_paths)