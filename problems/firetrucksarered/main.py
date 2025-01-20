def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(a, b, parent):
    root_a = find(a, parent)
    root_b = find(b, parent)
    if root_a != root_b:
        parent[root_b] = root_a

def solve(n, descriptions):
    parent = list(range(n))
    
    for i in range(n):
        numbers = descriptions[i]
        for j in range(1, len(numbers)):
            union(i, numbers[j] - 1, parent)
    
    root_set = set()
    for i in range(n):
        root_i = find(i, parent)
        root_set.add(root_i)
    
    if len(root_set) == 1:
        for i in range(1, n):
            print(f"{i + 1} {find(i, parent) + 1} {descriptions[i][0]}")
    else:
        print("impossible")

# Read input
n = int(input().strip())
descriptions = [list(map(int, input().strip().split())) for _ in range(n)]
solve(n, descriptions)