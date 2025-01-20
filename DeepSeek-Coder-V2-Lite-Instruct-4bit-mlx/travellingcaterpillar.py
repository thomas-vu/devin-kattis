def read_ints():
    return list(map(int, input().split()))

N, K = read_ints()
edges = [[] for _ in range(N)]
for _ in range(N - 1):
    s, t, d = read_ints()
    edges[s].append((t, d))
    edges[t].append((s, d))

leaves = read_ints()

# Function to perform DFS and calculate distances from the root
def dfs(node, parent):
    if node in leaves:
        dist[node] = 0
    for child, weight in edges[node]:
        if child != parent:
            dfs(child, node)
            dist[node] += dist[child] + weight

# Initialize distance array
dist = [0] * N
dfs(0, -1)

# Calculate the total distance Lilith must travel to eat all leaves
total_distance = sum(dist[leaf] for leaf in leaves)
print(total_distance)