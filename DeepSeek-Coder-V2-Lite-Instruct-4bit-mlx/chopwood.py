def find_parent(v, edges):
    for edge in edges:
        if edge[1] == v:
            return edge[0]
    return None

n = int(input())
v_column = [int(input()) for _ in range(n)]
edges = []
for i in range(1, n + 1):
    edges.append((i, v_column[i - 1]))

parents = [0] * (n + 1)
for edge in edges:
    child, parent = edge
    parents[child] = parent

u_column = []
for i in range(1, n + 1):
    current = parents[i]
    while find_parent(current, edges) is not None:
        current = find_parent(current, edges)
    u_column.append(current)

for u in u_column:
    print(u)