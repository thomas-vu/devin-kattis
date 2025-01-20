import sys
from math import pi, cos, sin, atan2, sqrt

def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0

def paint_used(vertices):
    n = len(vertices)
    total_area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total_area += (x1 * y2 - x2 * y1) / 2.0
    return total_area

def main():
    n = int(input().strip())
    polygons = []
    for _ in range(n):
        m = int(input().strip())
        vertices = []
        for _ in range(m):
            x, y = map(int, input().strip().split())
            vertices.append((x, y))
        polygons.append(vertices)
    
    total_paint = 0.0
    total_canvas = 0.0
    
    for vertices in polygons:
        area = polygon_area(vertices)
        total_paint += area
        total_canvas += paint_used(vertices)
    
    print("{:.8f} {:.8f}".format(total_paint, total_canvas))

if __name__ == "__main__":
    main()