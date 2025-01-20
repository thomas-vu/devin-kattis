def can_create_problemset(a, b, c, n):
    if a < 1 or b < 1 or c < 1:
        return 'NO'
    total_problems = a + b + c
    if total_problems < n or (n - (a + b + c)) % 3 != 0:
        return 'NO'
    return 'YES'

# Read input
a, b, c, n = map(int, input().split())
print(can_create_problemset(a, b, c, n))