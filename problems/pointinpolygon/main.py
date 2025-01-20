def is_point_in_polygon(polygon, point):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if point[1] > min(p1y, p2y):
            if point[1] <= max(p1y, p2y):
                if point[0] <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (point[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or point[0] <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        polygon = [tuple(map(int, input().split())) for _ in range(n)]
        m = int(input())
        points_to_test = [tuple(map(int, input().split())) for _ in range(m)]
        for point in points_to_test:
            if is_point_in_polygon(polygon, point):
                print("in")
            else:
                print("out" if not on_polygon(polygon, point) else "on")

def on_polygon(polygon, point):
    n = len(polygon)
    for i in range(n):
        p1x, p1y = polygon[i]
        p2x, p2y = polygon[(i + 1) % n]
        if min(p1y, p2y) <= point[1] <= max(p1y, p2y):
            if min(p1x, p2x) <= point[0] <= max(p1x, p2x):
                if (p2y - p1y) * (point[0] - p1x) == (p2x - p1x) * (point[1] - p1y):
                    return True
    return False

if __name__ == "__main__":
    main()