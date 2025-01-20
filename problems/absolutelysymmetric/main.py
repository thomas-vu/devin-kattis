def is_abs_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(matrix[i][j]) != abs(matrix[j][i]):
                return False
    return True

def decompose_matrix(matrix):
    n = len(matrix)
    decompositions = []
    
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != -matrix[j][i]:
                continue
            
            X = [[0] * n for _ in range(n)]
            X[i][j] = matrix[i][j]
            X[j][i] = -matrix[i][j]
            
            if is_abs_symmetric(X):
                decompositions.append(X)
    
    if not decompositions:
        return -1
    
    min_decompositions = len(decompositions)
    best_decomposition = decompositions[:]
    
    for mask in range(1, 1 << len(decompositions)):
        current_decomposition = []
        for j in range(len(decompositions)):
            if mask & (1 << j):
                current_decomposition.append(decompositions[j])
        
        if is_abs_symmetric(sum(current_decomposition, [[0] * n for _ in range(n)])):
            if len(current_decomposition) < min_decompositions:
                min_decompositions = len(current_decomposition)
                best_decomposition = current_decomposition[:]
    
    return min_decompositions, best_decomposition

def main():
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    
    result = decompose_matrix(matrix)
    if result == -1:
        print(-1)
    else:
        k, decompositions = result
        print(k)
        for decomposition in decompositions:
            for row in decomposition:
                print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()