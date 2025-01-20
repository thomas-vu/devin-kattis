def read_ints():
    return list(map(int, input().split()))

N, E = read_ints()
edges = [[] for _ in range(N)]
for _ in range(E):
    a, b = read_ints()
    edges[a].append(b)
    edges[b].append(a)

order = read_ints()

if order[0] != 0:
    print("NO")
else:
    seen = [False] * N
    current_order = 0
    
    def dfs(v):
        nonlocal current_order
        if seen[v]:
            return
        seen[v] = True
        for neighbour in sorted(edges[v]):
            if not seen[neighbour]:
                dfs(neighbour)
        nonlocal current_order
        if order[current_order] != v:
            print("NO")
            exit()
        current_order += 1
    
    dfs(0)
    
    if current_order == N:
        print("YES")
    else:
        print("NO")