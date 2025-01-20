def count_intersections(n, lines):
    intersections = 0
    for i in range(n):
        for j in range(i + 1, n):
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]
            if (x1 != x2 or y1 != y2) and (x3 != x4 or y3 != y4):
                denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
                if denom != 0:
                    ua = ((x3 - x4) * (y1 - y3) - (y3 - y4) * (x1 - x3)) / denom
                    ub = ((x1 - x2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / denom
                    if 0 <= ua <= 1 and 0 <= ub <= 1:
                        intersections += 1
    return intersections

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
print(count_intersections(n, lines))