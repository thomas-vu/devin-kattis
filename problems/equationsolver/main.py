import sys

def gauss_jordan(A, b):
    n = len(A)
    augmented_matrix = [a + [b[i]] for i, a in enumerate(A)]
    
    # Forward elimination
    for i in range(n):
        max_row = i + max(range(i, n), key=lambda x: abs(augmented_matrix[x][i]))
        augmented_matrix[i], augmented_matrix[max_row] = augmented_matrix[max_row][:], augmented_matrix[i][:]
        
        if abs(augmented_matrix[i][i]) < 1e-6:
            continue
        
        for j in range(n):
            if i != j:
                factor = augmented_matrix[j][i] / augmented_matrix[i][i]
                augmented_matrix[j] = [augmented_matrix[j][k] - factor * augmented_matrix[i][k] for k in range(n + 1)]
    
    # Back substitution
    solutions = [0] * n
    for i in range(n):
        if abs(augmented_matrix[i][i]) < 1e-6:
            if abs(augmented_matrix[i][n]) < 1e-6:
                return "multiple"
            else:
                return "inconsistent"
        solutions[i] = augmented_matrix[i][n] / augmented_matrix[i][i]
    
    return solutions

while True:
    n = int(input().strip())
    if n == 0:
        break
    
    A = []
    for _ in range(n):
        row = list(map(float, input().strip().split()))
        A.append(row)
    
    b = list(map(float, input().strip().split()))
    
    result = gauss_jordan(A, b)
    if result == "multiple":
        print("multiple")
    elif result == "inconsistent":
        print("inconsistent")
    else:
        for x in result:
            print("{:.6f}".format(x))