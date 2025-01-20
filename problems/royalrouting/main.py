MOD = 10**9 + 7

def multiply_matrix(a, b):
    result = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] = (result[i][j] + a[i][k] * b[k][j]) % MOD
    return result

def matrix_power(matrix, n):
    result = [[0]*8 for _ in range(8)]
    identity = [[int(i==j) for j in range(8)] for i in range(8)]
    current = identity.copy()
    
    while n > 0:
        if n % 2 == 1:
            current = multiply_matrix(current, matrix)
        matrix = multiply_matrix(matrix, matrix)
        n //= 2
    return current

# Define the transition matrix for the king's movement
king_moves = [
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Read input
n = int(input().strip())

# Calculate the nth power of the transition matrix
result_matrix = matrix_power(king_moves, n)

# The number of ways to reach H8 from A1 in exactly n steps is the top-right element of the result matrix
answer = result_matrix[0][7]
print(answer)