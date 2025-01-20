def reverse_number(n):
    return int(str(n)[::-1])

A, B = map(int, input().split())
reversed_A = reverse_number(A)
reversed_B = reverse_number(B)

print(max(reversed_A, reversed_B))