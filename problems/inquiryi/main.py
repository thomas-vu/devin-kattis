import sys

def solve(n, a):
    max_sum = 0
    for k in range(1, n):
        left_sum = sum(a[i]**2 for i in range(k))
        right_sum = sum(a[i] for i in range(k, n))
        max_sum = max(max_sum, left_sum * right_sum)
    return max_sum

# Read input from stdin
n = int(sys.stdin.readline().strip())
a = [int(sys.stdin.readline().strip()) for _ in range(n)]

# Solve the problem and print the result
print(solve(n, a))