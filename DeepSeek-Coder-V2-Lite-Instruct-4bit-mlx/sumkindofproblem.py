P = int(input())
for _ in range(P):
    K, N = map(int, input().split())
    S1 = (N * (N + 1)) // 2
    S2 = N ** 2
    S3 = N * (N + 1)
    print(K, S1, S2, S3)