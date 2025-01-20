def rectangles_intersect(rectangles):
    for i in range(len(rectangles)):
        for j in range(i + 1, len(rectangles)):
            r1 = rectangles[i]
            r2 = rectangles[j]
            if not (r1[2] < r2[0] or r1[3] < r2[1] or r2[2] < r1[0] or r2[3] < r1[1]):
                return 1
    return 0

n = int(input())
rectangles = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))

print(rectangles_intersect(rectangles))