import sys
sys.setrecursionlimit(10**6)

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    elif rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

N, M, Q = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
queries = [list(map(int, input().split())) for _ in range(Q)]

# Reverse edges and queries to process them later
edges = edges[::-1]
queries = queries[::-1]

# Initialize data structures for disjoint set and answer list
parent = [i for i in range(N)]
rank = [0] * N
answer = []

# Process edges in reverse order and handle queries in reverse order
for t, u, v in queries:
    if t == 0:
        # Union the edge (u, v)
        union(u, v)
    else:
        # Check if u and v are in the same connected component
        if find(u) == find(v):
            answer.append("safe")
        else:
            answer.append("unsafe")

# Reverse the answers to match the original order of queries
answer = answer[::-1]

# Output the answers for the final queries
for ans in answer:
    print(ans)