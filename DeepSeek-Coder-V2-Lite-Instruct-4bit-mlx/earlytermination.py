def euclid(a, b, k):
    while a > k or b > k:
        if a < b:
            a, b = b, a
        a %= b
    return (a, b) if a > b else (b, a)

# Read input
a, b, k = map(int, input().split())
result = euclid(a, b, k)
print(*result)