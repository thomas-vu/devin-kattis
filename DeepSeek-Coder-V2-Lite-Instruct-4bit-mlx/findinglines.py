def can_find_line(n, p, points):
    threshold = int(n * (p / 100))
    lines = set()
    
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2:  # Vertical line
                lines.add(f'{x1}')
            else:
                a = (y2 - y1) / (x2 - x1)
                b = y1 - a * x1
                lines.add(f'{a},{b}')
    
    if len(lines) >= threshold:
        return "possible"
    else:
        return "impossible"

# Read input
n = int(input())
p = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Determine if a suitable line exists
result = can_find_line(n, p, points)
print(result)