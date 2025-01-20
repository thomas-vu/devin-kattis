def is_inside(x, y, rect):
    x1, y1, x2, y2 = rect
    return x1 <= x <= x2 and y1 <= y <= y2

def is_inside_circle(x, y, cx, cy, r):
    return (cx - x)**2 + (cy - y)**2 <= r**2

m = int(input())
targets = []
for _ in range(m):
    shape, *params = input().split()
    if shape == 'rectangle':
        x1, y1, x2, y2 = map(int, params)
        targets.append((x1, y1, x2, y2))
    elif shape == 'circle':
        cx, cy, r = map(int, params)
        targets.append((cx, cy, r))

n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    count = 0
    for rect in targets:
        if isinstance(rect, tuple):
            x1, y1, x2, y2 = rect
            if x1 <= x <= x2 and y1 <= y <= y2:
                count += 1
        else:
            cx, cy, r = rect
            if is_inside_circle(x, y, cx, cy, r):
                count += 1
    print(count)