import sys
from typing import List, Tuple

MOD = 10**9 + 7

def matrix_mult(A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
    return result

def matrix_pow(A: List[List[int]], k: int) -> List[List[int]]:
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        result[i][i] = 1
    while k > 0:
        if k % 2 == 1:
            result = matrix_mult(result, A)
        A = matrix_mult(A, A)
        k //= 2
    return result

def read_ints() -> List[int]:
    return list(map(int, sys.stdin.readline().strip().split()))

n, m, k = read_ints()
matrix = [read_ints() for _ in range(n)]
s = read_ints()[0]
start_states = read_ints()
end_states = read_ints()

# Convert start and end states to indices in the matrix
start_indices = [state for state in start_states]
end_indices = [state for state in end_states]

# Find the submatrix corresponding to start and end states
submatrix = [[0] * n for _ in range(n)]
for i in start_indices:
    for j in end_states:
        submatrix[i][j] = matrix[i][j]

# Compute the k-th power of the submatrix
submatrix_pow = matrix_pow(submatrix, k)

# The result is the sum of the submatrix entries for end states
result = 0
for i in end_indices:
    result = (result + submatrix_pow[start_indices[0]][i]) % MOD

print(result)