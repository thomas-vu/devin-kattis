N, M = map(int, input().split())
MOD = 10**9 + 7
A = [0] * N

def query_type_0(x, y):
    sum_mod = 0
    for i in range(x - 1, y):
        sum_mod = (sum_mod + A[i]) % MOD
    print(sum_mod)

def query_type_1(x, y):
    for i in range(y - x + 1):
        A[x + i - 1] += (i + 1) * (i + 2) * (i + 3)
        A[x + i - 1] %= MOD

def query_type_2(x, y):
    for i in range(y - x + 1):
        A[x + i - 1] -= (i + 1) * (i + 2) * (i + 3)
        A[x + i - 1] %= MOD

for _ in range(M):
    t, x, y = map(int, input().split())
    if t == 0:
        query_type_0(x, y)
    elif t == 1:
        query_type_1(x, y)
    elif t == 2:
        query_type_2(x, y)