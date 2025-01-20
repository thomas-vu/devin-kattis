def is_right_triangle(a, b, c):
    sides = [a, b, c]
    sides.sort()
    return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-9

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    if is_right_triangle(a, b, c):
        print("right")
    else:
        print("wrong")