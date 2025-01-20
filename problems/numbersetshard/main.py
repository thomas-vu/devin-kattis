import math

def sieve(max_num):
    prime = [True for _ in range(max_num + 1)]
    p = 2
    while (p * p <= max_num):
        if prime[p]:
            for i in range(p * p, max_num + 1, p):
                prime[i] = False
        p += 1
    return [p for p in range(2, max_num + 1) if prime[p]]

def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]

def union(a, b, parent, rank):
    rootA = find_parent(a, parent)
    rootB = find_parent(b, parent)
    if rootA != rootB:
        if rank[rootA] > rank[rootB]:
            parent[rootB] = rootA
        elif rank[rootA] < rank[rootB]:
            parent[rootA] = rootB
        else:
            parent[rootB] = rootA
            rank[rootA] += 1

def solve(case_num, A, B, P):
    prime_numbers = sieve(int(math.sqrt(B)) + 1)
    parent = {i: i for i in range(A, B + 1)}
    rank = {i: 0 for i in range(A, B + 1)}
    
    for i in range(A, B + 1):
        for prime in prime_numbers:
            if i % prime == 0 and i // prime >= A:
                union(i, i // prime, parent, rank)
    
    root_set = set()
    for i in range(A, B + 1):
        root_set.add(find_parent(i, parent))
    
    return len(root_set)

def main():
    C = int(input())
    for case_num in range(1, C + 1):
        A, B, P = map(int, input().split())
        result = solve(case_num, A, B, P)
        print("Case #{}: {}".format(case_num, result))

if __name__ == "__main__":
    main()