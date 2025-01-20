a, b, c = map(int, input().split())
d = 2 * b - a - c if a != b and b != c else (a + c) / 2
print(int(d))