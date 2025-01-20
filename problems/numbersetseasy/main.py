def find_parent(parent, i):
    if parent[i] != i:
        parent[i] = find_parent(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    C = int(data[0])
    index = 1
    results = []
    
    for case in range(1, C + 1):
        A = int(data[index])
        B = int(data[index + 1])
        P = int(data[index + 2])
        index += 3
        
        parent = [i for i in range(B - A + 1)]
        rank = [0] * (B - A + 1)
        
        for i in range(A, B):
            for j in range(i + 1, B + 1):
                if is_prime(j) and i % j == 0:
                    union(parent, rank, i - A, j - A)
        
        set_count = sum(1 for i in range(B - A + 1) if find_parent(parent, i) == i)
        results.append(f"Case #{case}: {set_count}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()