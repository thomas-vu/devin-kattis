def main():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    
    edges = []
    for i in range(N):
        for j in range(i+1, N):
            if A[i][j] != A[i][0]:  # Check if the edge exists in the reconstructed map
                edges.append((A[i][0], A[j][0]))
    
    for edge in edges:
        print(edge[0], edge[1])

if __name__ == "__main__":
    main()