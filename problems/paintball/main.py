def read_ints():
    return list(map(int, input().split()))

N, M = read_ints()
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = read_ints()
    graph[A].append(B)
    graph[B].append(A)

targets = [0] * (N + 1)
for i in range(1, N + 1):
    for target in graph[i]:
        if targets[target] == 0 and i != target:
            targets[i] = target
            break

if 0 in targets[1:]:
    print("Impossible")
else:
    for i in range(1, N + 1):
        print(targets[i])