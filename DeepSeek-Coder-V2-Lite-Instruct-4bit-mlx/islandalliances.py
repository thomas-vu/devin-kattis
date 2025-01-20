n, m, q = map(int, input().split())
distrust_pairs = [tuple(map(int, input().split())) for _ in range(m)]
proposals = [tuple(map(int, input().split())) for _ in range(q)]

# Initialize parent and rank arrays for DSU
parent = list(range(n + 1))
rank = [0] * (n + 1)

# Function to find the parent of a node
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Function to merge two sets
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True
    return False

# Process distrust pairs to initialize states
for u, v in distrust_pairs:
    union(u, v)

# Process proposals to check if they should be approved or refused
results = []
for a, b in proposals:
    if find(a) == find(b):
        results.append("APPROVE")
    else:
        results.append("REFUSE")

# Output the results
for result in results:
    print(result)