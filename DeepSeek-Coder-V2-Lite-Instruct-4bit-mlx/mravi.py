def read_ints():
    return list(map(int, input().split()))

N = int(input())
edges = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, X, T = read_ints()
    edges[A].append((B, X, T))
    edges[B].append((A, X, T))

K = read_ints()

def dfs(node, parent):
    if K[node - 1] == -1:
        for child, flow, has_superpower in edges[node]:
            if child != parent:
                dfs(child, node)
    else:
        flow_matrix[node] = K[node - 1]
    
    for child, flow, has_superpower in edges[node]:
        if child != parent:
            dfs(child, node)
            if has_superpower == 1:
                flow_matrix[node] = flow_matrix[node] * (flow / 100)
            else:
                flow_matrix[node] = flow_matrix[node] * (flow / 100)
    
    if K[node - 1] == -1:
        for child, flow, has_superpower in edges[node]:
            if child != parent:
                flow_matrix[node] += flow_matrix[child]
    
    if K[node - 1] == -1:
        flow_matrix[node] = min(flow_matrix[node], K[node - 1])

flow_matrix = [0] * (N + 1)
dfs(1, -1)
print("{:.8f}".format(flow_matrix[1]))