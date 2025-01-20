MOD = 10**9 + 7
def calculate_fibonacci(x, y):
    F = [[0] * (y + 2) for _ in range(x + 2)]
    F[0][1] = 1
    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 and j == 0:
                continue
            F[i + 1][j + 1] = (F[i][j + 1] + F[i + 1][j]) % MOD
    return F[x + 1][y + 1]
x, y = map(int, input().split())
print(calculate_fibonacci(x, y))