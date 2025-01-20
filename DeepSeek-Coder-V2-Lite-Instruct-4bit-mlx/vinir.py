def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

N, Q = map(int, input().split())
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
friends = {}

for _ in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        a, b = query[1], query[2]
        union(parent, rank, a, b)
    elif query[0] == 2:
        a = query[1]
        rootA = find(parent, a)
        for i in range(1, N + 1):
            if find(parent, i) == rootA:
                friends[a] = friends.get(a, 0) + 1

for i in range(1, N + 1):
    rootI = find(parent, i)
    friends[i] = friends.get(i, 0) + len([j for j in range(1, N + 1) if find(parent, j) == rootI]) - 1

for i in range(Q):
    query = list(map(int, input().split()))
    
    if query[0] == 2:
        a = query[1]
        print(friends.get(a, 0))