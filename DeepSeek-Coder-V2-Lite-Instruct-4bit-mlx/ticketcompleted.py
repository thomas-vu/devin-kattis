# Read input
N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

# Create adjacency list
adj_list = [[] for _ in range(N + 1)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Find connected components using DFS
visited = [False] * (N + 1)
def dfs(node):
    if visited[node]:
        return
    visited[node] = True
    for neighbor in adj_list[node]:
        dfs(neighbor)

# Count number of components and nodes in each component
num_components = 0
component_sizes = []
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        num_components += 1
        component_sizes.append(sum(visited))

# Calculate probability
total_tickets = N * (N - 1) // 2
claimed_edges = M
unclaimed_edges = total_tickets - claimed_edges

# Probability of earning points from a ticket is the ratio of unclaimed pairs to total pairs
probability = (unclaimed_edges / total_tickets) if total_tickets != 0 else 0
print("{:.15f}".format(probability))