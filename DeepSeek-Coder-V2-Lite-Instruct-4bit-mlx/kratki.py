def find_sequence(N, K):
    if K == 1:
        return [i for i in range(1, N + 1)] if N >= K else [-1]
    elif K == N:
        return [i for i in range(N, 0, -1)]
    else:
        sequence = [i for i in range(1, N + 1)]
        # Reverse the subsequence of length K to get a descending sequence
        for i in range(N - K + 1):
            if i % 2 == 0:
                sequence[i], sequence[N - K + i] = sequence[N - K + i], sequence[i]
        return sequence if K == 2 else [-1]

# Read input from stdin
N, K = map(int, input().split())
result = find_sequence(N, K)
# Output the result
print(' '.join(map(str, result)))