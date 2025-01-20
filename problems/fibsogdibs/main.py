MOD = 10**9 + 7

def fibs_dibs(a, b, n):
    if n == 0:
        return a % MOD, b % MOD
    elif n == 1:
        return b % MOD, (a + b) % MOD
    else:
        x, y = 1, 1
        for _ in range(2, n + 1):
            x, y = y, (x + y) % MOD
        return y % MOD, (a * x + b * y) % MOD

# Read input
a, b = map(int, input().split())
n = int(input())

# Calculate the result
result = fibs_dibs(a, b, n)

# Output the result
print(*result)