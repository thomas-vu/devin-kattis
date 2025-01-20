def count_letters(K):
    a, b = 1, 0
    for _ in range(K):
        a, b = b, a + b
    return a, b

K = int(input())
A, B = count_letters(K)
print(A, B)