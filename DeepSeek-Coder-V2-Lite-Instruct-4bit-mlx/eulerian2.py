def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()
edges = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    a, b = read_ints()
    edges[a].append(b)

W = int(input())
walk = read_ints()
passed_edges = set()

for i in range(W):
    if walk[i] not in edges or walk[i+1] not in edges[walk[i]]:
        print(f"invalid {i + 1}")
        break
    if (walk[i], walk[i+1]) not in passed_edges:
        passed_edges.add((walk[i], walk[i+1]))
else:
    if len(passed_edges) < M:
        print("too short")
    else:
        print("correct")