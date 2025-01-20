import sys
from itertools import combinations

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p1[1] - p3[1]) * (p2[0] - p3[0])

def is_inside(polygon, point):
    n = len(polygon)
    if sign(point, polygon[0], polygon[1]) < 0:
        return False
    if sign(point, polygon[-1], polygon[0]) > 0:
        return False
    left = 1
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if sign(point, polygon[mid], polygon[0]) < 0:
            right = mid - 1
        else:
            left = mid + 1
    i = right
    t = (point[0] - polygon[i][0]) * (polygon[(i + 1) % n][1] - polygon[i][1]) - (point[1] - polygon[i][1]) * (polygon[(i + 1) % n][0] - polygon[i][0])
    return t > 0

def area(polygon):
    n = len(polygon)
    a = 0.0
    for i in range(n):
        j = (i + 1) % n
        a += polygon[i][0] * polygon[j][1] - polygon[j][0] * polygon[i][1]
    return abs(a) / 2.0

def main():
    n, m = map(int, input().split())
    polygon = [tuple(map(float, input().split())) for _ in range(n)]
    lines = [tuple(map(float, input().split())) for _ in range(m)]
    
    max_area = 0.0
    for i in range(m):
        for j in range(i + 1, m):
            line = lines[i], lines[j]
            polygons = set()
            for k in range(n):
                if sign(polygon[k], lines[i], lines[j]) == 0:
                    continue
                new_polygon = []
                for l in range(n):
                    if sign(polygon[l], lines[i], lines[j]) > 0:
                        new_polygon.append(polygon[l])
                if len(new_polygon) > 0:
                    polygons.add(tuple(new_polygon))
            for k in range(n):
                if sign(polygon[k], lines[i], lines[j]) < 0:
                    new_polygon = []
                    for l in range(n):
                        if sign(polygon[l], lines[i], lines[j]) < 0:
                            new_polygon.append(polygon[l])
                    if len(new_polygon) > 0:
                        polygons.add(tuple(new_polygon))
            for polygon in polygons:
                max_area = max(max_area, area(polygon))
    print("{:.10f}".format(max_area))

if __name__ == "__main__":
    main()