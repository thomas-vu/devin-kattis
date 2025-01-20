def max_kilometers(N, K):
    if N <= K:
        return 1 + (N - 1) * 2
    else:
        left = N // K
        right = (N - (left * K)) + min(K, left)
        return left * 2 + right - 1

# Read input
N, K = map(int, input().split())
print(max_kilometers(N, K))