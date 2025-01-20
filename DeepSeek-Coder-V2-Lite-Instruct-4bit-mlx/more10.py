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

def are_statements_consistent(statements):
    parent = {}
    rank = {}
    
    for statement in statements:
        x, y = statement.split()
        if x not in parent:
            parent[x] = x
            rank[x] = 0
        if y not in parent:
            parent[y] = y
            rank[y] = 0
        
        if find(parent, x) == find(parent, y):
            continue
        
        if (x + ' is ' + y) in statements or (y + ' is ' + x) in statements:
            union(parent, rank, x, y)
        else:
            return "wait what?"
    
    for statement in statements:
        x, y = statement.split()
        if (x + ' is not ' + y) in statements or (y + ' is not ' + x) in statements:
            if find(parent, x) == find(parent, y):
                return "wait what?"
    
    return "yes"

# Read input
N = int(input())
statements = [input().strip() for _ in range(N)]

# Output the result
print(are_statements_consistent(statements))