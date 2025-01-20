def min_sum(N, A, B):
    min_value = float('inf')
    for L in range(N):
        sumA = 0
        sumB = 0
        for R in range(L, N):
            sumA += A[R]
            sumB += B[R]
            min_value = min(min_value, sumA**2 + sumB**2)
    return min_value

# Read input from stdin
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Output the result
print(min_sum(N, A, B))