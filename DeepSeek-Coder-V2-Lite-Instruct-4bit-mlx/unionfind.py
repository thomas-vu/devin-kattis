def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def main():
    N, Q = map(int, input().split())
    parent = list(range(N))
    rank = [0] * N
    
    for _ in range(Q):
        op, a, b = input().split()
        a, b = int(a), int(b)
        
        if op == '=':
            union(parent, rank, a, b)
        else:  # op == '?'
            if find(parent, a) == find(parent, b):
                print("yes")
            else:
                print("no")

if __name__ == "__main__":
    main()