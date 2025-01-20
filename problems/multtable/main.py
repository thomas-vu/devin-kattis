def count_occurrences(N, M):
    count = 0
    for i in range(1, N + 1):
        if M % i == 0:
            j = M // i
            if j <= N:
                count += 1
    return count

# Read input
N, M = map(int, input().split())

# Calculate the number of occurrences
result = count_occurrences(N, M)

# Output the result
print(result)