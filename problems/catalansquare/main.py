def catalan(n):
    if n == 0 or n == 1:
        return 1
    C = [0] * (n + 1)
    C[0], C[1] = 1, 1
    for i in range(2, n + 1):
        for j in range(i):
            C[i] += C[j] * C[i - j - 1]
    return C[n]

def calculate_S(n):
    S = [0] * (n + 1)
    for i in range(n + 1):
        S[i] = catalan(i) * catalan(i)
    return sum(S)

n = int(input().strip())
print(calculate_S(n))