import sys

# Read input
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

# Initialize the result array B
B = [0] * n

# Apply the erosion filter
for i in range(n):
    total_weight = 0
    weighted_sum = 0
    for j in range(n):
        weight = 1 / (2 ** abs(i - j))
        weighted_sum += A[j] * weight
        total_weight += weight
    B[i] = weighted_sum / total_weight

# Output the result with precision 5
for value in B:
    print("{:.6f}".format(value), end=' ')