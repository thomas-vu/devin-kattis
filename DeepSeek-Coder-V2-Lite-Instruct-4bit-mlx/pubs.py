from sys import stdin, stdout

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

def solve(n, m, edges):
    parent = [i for i in range(n + 1)]
    rank = [0] * (n + 1)
    
    for edge in edges:
        u, v = edge
        union(parent, rank, u, v)
    
    pub_count = 0
    house_count = 0
    
    for i in range(1, n + 1):
        root = find(parent, i)
        if root == 1:
            pub_count += 1
        else:
            house_count += 1
    
    if pub_count == 0 or house_count == 0:
        return "Impossible"
    
    result = []
    for i in range(1, n + 1):
        root = find(parent, i)
        if root == 1:
            result.append("pub")
        else:
            result.append("house")
    
    return " ".join(result)

# Read input
n, m = map(int, stdin.readline().strip().split())
edges = [tuple(map(int, stdin.readline().strip().split())) for _ in range(m)]

# Solve the problem and print output
stdout.write(solve(n, m, edges))