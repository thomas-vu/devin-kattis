def fibonacci_sequence(k, M):
    F = [1, 2]
    for i in range(2, k):
        F.append((F[-1] + F[-2]) % M)
    return F[:k]

def solve_test_case(k, M, p):
    F = fibonacci_sequence(k + 1, M)
    matrix = [[F[i]**j for j in range(k)] for i in range(k)]
    constants = [p[i] for i in range(k)]
    
    # Gaussian elimination to solve the system of linear equations
    for i in range(k):
        factor = matrix[i][i]
        for j in range(i, k):
            matrix[i][j] = (matrix[i][j] * pow(factor, M-2, M)) % M
        constants[i] = (constants[i] * pow(factor, M-2, M)) % M
        
        for row in range(k):
            if i != row:
                factor = matrix[row][i]
                for j in range(i, k):
                    matrix[row][j] = (matrix[row][j] - matrix[i][j] * factor) % M
                constants[row] = (constants[row] - constants[i] * factor) % M
    
    # The solution is the constant term for F_{k+1}
    return constants[-1]

def main():
    T = int(input())
    results = []
    for _ in range(T):
        k, M = map(int, input().split())
        p = list(map(int, input().split()))
        results.append(solve_test_case(k, M, p))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()