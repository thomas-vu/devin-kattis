def can_order(m, a, b, c):
    return "possible" if m > a + b + c else "impossible"

# Read input from stdin
m, a, b, c = map(int, input().split())
print(can_order(m, a, b, c))