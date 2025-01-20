import sys
from math import sqrt, fabs

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_inside_polygon(x, y, points):
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xints = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xints:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def distance_point_to_segment(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx != 0 or dy != 0:
        u = ((px - x1) * dx + (py - y1) * dy) / (dx * dx + dy * dy)
        if u > 1:
            u = 1
        elif u < 0:
            u = 0
        xu = x1 + u * dx
        yu = y1 + u * dy
        return sqrt((px - xu) ** 2 + (py - yu) ** 2)
    else:
        return sqrt((px - x1) ** 2 + (py - y1) ** 2)

def main():
    test_case = 0
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().strip().split())
            points.append((x, y))
        s = int(sys.stdin.readline().strip())
        shots = []
        for _ in range(s):
            x, y = map(int, sys.stdin.readline().strip().split())
            shots.append((x, y))
        test_case += 1
        print(f"Case {test_case}")
        for shot in shots:
            if point_inside_polygon(*shot, points):
                print("Hit!", end=' ')
                min_dist = float('inf')
                for i in range(n):
                    p1 = points[i]
                    p2 = points[(i + 1) % n]
                    dist = distance_point_to_segment(*shot, *p1, *p2)
                    if fabs(dist) < 1e-7:
                        print("Winged!")
                        break
                    if dist < min_dist:
                        min_dist = dist
                else:
                    print(f"{min_dist:.9f}")
            else:
                dist = distance_point_to_segment(*shot, *points[0], *points[-1])
                if fabs(dist) < 1e-7:
                    print("Winged!")
                else:
                    print("Miss!", end=' ')
                    print(f"{dist:.9f}")

if __name__ == "__main__":
    main()