def right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        return sides[0] * sides[1] / 2
    else:
        return -1

# Read input from stdin
a, b, c = map(int, input().split())
result = right_triangle(a, b, c)
print(result)