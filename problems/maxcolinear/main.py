def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def max_colinear_points(points):
    if len(points) <= 2:
        return len(points)
    
    max_count = 0
    for i in range(len(points)):
        slopes = {}
        duplicates = 1
        for j in range(len(points)):
            if i == j:
                continue
            if points[i] == points[j]:
                duplicates += 1
            else:
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                g = gcd(dx, dy)
                slope = (dx // g, dy // g)
                slopes[slope] = slopes.get(slope, 0) + 1
        max_count = max(max_count, duplicates)
        for slope in slopes:
            max_count = max(max_count, slopes[slope] + duplicates)
    return max_count

while True:
    n = int(input())
    if n == 0:
        break
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(max_colinear_points(points))