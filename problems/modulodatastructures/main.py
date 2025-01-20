N, Q = map(int, input().split())
Arr = [0] * (N + 1)

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A, B, C = query[1], query[2], query[3]
        for k in range(A, N + 1, B):
            Arr[k] += C
    else:
        D = query[1]
        print(Arr[D])