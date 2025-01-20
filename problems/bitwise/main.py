def max_bitwise_and(N, K, A):
    def power_of_section(start, end):
        result = 0
        for i in range(start, end + start):
            result |= A[i % N]
        return result

    max_and = 0
    for i in range(N):
        sections = []
        for j in range(K - 1):
            sections.append((i + j * (N // K), i + (j + 1) * (N // K) - 1))
        sections.append((i + (K - 1) * (N // K), N - 1))
        current_and = float('inf')
        for section in sections:
            start, end = section
            current_and &= power_of_section(start, end)
        max_and = max(max_and, current_and)
    return max_and

# Read input
import sys
input = sys.stdin.read
data = input().split()
N, K = int(data[0]), int(data[1])
A = list(map(int, data[2:]))

# Output the result
print(max_bitwise_and(N, K, A))