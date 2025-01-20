def find_jumps(S, x, y, dx, dy):
    jumps = 0
    while True:
        x += dx
        y += dy
        jumps += 1
        if (x % S == 0 and y % S != 0) or (x % S != 0 and y % S == 0):
            return f"After {jumps} jumps the flea lands at ({x}, {y})."
        if x > 10**6 or y > 10**6:
            return "The flea cannot escape from black squares."

while True:
    S, x, y, dx, dy = map(int, input().split())
    if S == 0 and x == 0 and y == 0 and dx == 0 and dy == 0:
        break
    print(find_jumps(S, x, y, dx, dy))