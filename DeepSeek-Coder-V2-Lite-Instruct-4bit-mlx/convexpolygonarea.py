def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    return abs(area) / 2.0

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        vertices = []
        for _ in range(m):
            x, y = map(int, input().split())
            vertices.append((x, y))
        area = calculate_polygon_area(vertices)
        print("{:.1f}".format(area))

if __name__ == "__main__":
    main()