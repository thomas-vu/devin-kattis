def find_drawer(A, B, parent):
    if parent[A] == A:
        return A
    else:
        parent[A] = find_drawer(parent[A], B, parent)
        return parent[A]

def main():
    N, L = map(int, input().split())
    parent = list(range(L + 1))
    
    for _ in range(N):
        A_i, B_i = map(int, input().split())
        rootA = find_drawer(A_i, B_i, parent)
        if rootA == A_i:
            print("LADICA")
            parent[rootA] = find_drawer(B_i, B_i, parent)
        elif rootA == B_i:
            print("LADICA")
            parent[rootA] = find_drawer(A_i, A_i, parent)
        else:
            print("SMECE")

if __name__ == "__main__":
    main()