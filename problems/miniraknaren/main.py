def min_operations(N, M):
    if N == 0:
        return 0
    
    operations = [float('inf')] * (N + M)
    operations[0] = 0
    
    for i in range(N + M):
        if operations[i] != float('inf'):
            # Multiply by 2
            for j in range(i + 1, min(N + M, i + (M - 1) * 2 + 1)):
                operations[j] = min(operations[j], operations[i] + 2)
            # Multiply by 3
            for j in range(i + 1, min(N + M, i + (M - 1) * 3 + 1)):
                operations[j] = min(operations[j], operations[i] + 3)
            # Add M - 1
            for j in range(i + (M - 1), min(N + M, i + (M - 1) * 2)):
                operations[j] = min(operations[j], operations[i] + 2)
            # Add M - 2
            for j in range(i + (M - 2), min(N + M, i + (M - 1) * 3)):
                operations[j] = min(operations[j], operations[i] + 3)
    
    return operations[N] if operations[N] != float('inf') else -1

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])

# Get the result and print it
result = min_operations(N, M)
print(result)