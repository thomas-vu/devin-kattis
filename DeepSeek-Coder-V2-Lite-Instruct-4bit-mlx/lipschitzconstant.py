def find_lipshitz_constant(points):
    max_diff = 0
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            max_diff = max(max_diff, abs(y2 - y1) / (abs(x2 - x1)))
    return max_diff

N = int(input())
points = [tuple(map(float, input().split())) for _ in range(N)]
print("{:.10f}".format(find_lipshitz_constant(points)))