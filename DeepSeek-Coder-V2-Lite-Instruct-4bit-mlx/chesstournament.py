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

def is_consistent(N, matches):
    parent = list(range(N))
    rank = [0] * N
    
    for match in matches:
        K, symbol, L = match
        if symbol == '=':
            union(parent, rank, K, L)
    
    for match in matches:
        if match[1] == '>':
            rootK = find(parent, K)
            rootL = find(parent, L)
            if rootK == rootL:
                return "inconsistent"
    
    for match in matches:
        if match[1] == '=':
            rootK = find(parent, K)
            rootL = find(parent, L)
            if rootK != rootL:
                union(parent, rank, K, L)
    
    for match in matches:
        rootK = find(parent, K)
        rootL = find(parent, L)
        if rootK == rootL and match[1] == '>':
            return "inconsistent"
    
    return "consistent"

# Read input
N, M = map(int, input().split())
matches = [tuple(input().split()) for _ in range(M)]
for i in range(M):
    matches[i] = (int(matches[i][0]), matches[i][1], int(matches[i][2]))

# Output result
print(is_consistent(N, matches))