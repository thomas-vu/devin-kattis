def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()
edges = [read_ints() for _ in range(M)]

# Create adjacency list to represent the graph
adj = {i: [] for i in range(1, N + 1)}
for a, b in edges:
    adj[a].append(b)
    adj[b].append(a)

# Check if the graph is traversable in Eulerian path order
def check_eulerian():
    odd_count = sum(len(neighbors) % 2 for neighbors in adj.values())
    if odd_count != 0 and odd_count != 2:
        return "impossible"
    return True

# Perform DFS to find the Eulerian path
def dfs(node, adj, path):
    while adj[node]:
        next_node = adj[node].pop()
        dfs(next_node, adj, path)
    path.append(node)

# Main logic to find the train lines
result = check_eulerian()
if result == "impossible":
    print(result)
else:
    path = []
    dfs(1, adj, path)
    for i in range(N - 1):
        if path[i] != i + 1:
            print("impossible")
            break
    else:
        for i in range(N):
            print(edges.index((path[i], path[(i + 1) % N]) if i < N - 1 else (path[i], path[0])) + 1)