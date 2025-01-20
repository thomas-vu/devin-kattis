def matrix_mult(a, b):
    res = [[0] * len(b[0]) for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                res[i][j] = (res[i][j] + a[i][k] * b[k][j]) % M
    return res

def matrix_pow(a, p):
    result = [[0] * len(a) for _ in range(len(a))]
    identity = [[1 if i == j else 0 for j in range(len(a))] for i in range(len(a))]
    while p > 0:
        if p % 2 == 1:
            identity = matrix_mult(identity, a)
        a = matrix_mult(a, a)
        p //= 2
    return identity

def solve():
    N = int(input())
    coefficients = list(map(int, input().split()))
    initial_values = list(map(int, input().split()))
    Q = int(input())
    
    # Transition matrix construction
    transition_matrix = [[0] * N for _ in range(N)]
    for i in range(N):
        transition_matrix[0][i] = coefficients[i + 1]
    for i in range(1, N):
        transition_matrix[i][i - 1] = 1
    
    # Initial vector construction
    initial_vector = [0] * N
    for i in range(N):
        if i < len(initial_values):
            initial_vector[i] = initial_values[-i - 1]
    
    # Matrix exponentiation to find x[T]
    T = int(input())
    if T < N:
        print(initial_values[N - 1 - T] % M)
    else:
        transition_matrix = matrix_pow(transition_matrix, T - N + 1)
        result_vector = [0] * N
        for i in range(N):
            for j in range(N):
                result_vector[i] = (result_vector[i] + transition_matrix[0][j] * initial_values[-j - 1]) % M
        print(result_vector[0] % M)
    
    # Process queries
    for _ in range(Q):
        T, M = map(int, input().split())
        solve()