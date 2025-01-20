import math

def find_right_triangle(n):
    for a in range(1, int(math.sqrt(n)) + 1):
        for b in range(a, int(math.sqrt(n)) + 1):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == n and int(c) == c:
                return (a, b, int(c))
    return (0, 0, 0)

n = int(input())
a, b, c = find_right_triangle(n)
print(a, b, c)