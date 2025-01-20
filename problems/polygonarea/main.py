import sys

def calculate_polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    area = abs(area) / 2.0
    return area

def determine_polygon_direction(vertices):
    n = len(vertices)
    sum1 = 0.0
    for i in range(n):
        j = (i + 1) % n
        sum1 += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    if sum1 > 0:
        return "CW"
    else:
        return "CCW"

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        vertices = []
        for _ in range(n):
            x, y = map(int, input().split())
            vertices.append((x, y))
        area = calculate_polygon_area(vertices)
        direction = determine_polygon_direction(vertices)
        print(f"{direction} {area:.1f}")

if __name__ == "__main__":
    main()