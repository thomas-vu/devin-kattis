import sys
from itertools import combinations

def calculate_area(p1, p2, p3):
    return abs((p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0])) / 2

def simplify_polyline(points, m):
    n = len(points) - 1
    while n > m:
        min_area = float('inf')
        remove_index = -1
        for i in range(1, n):
            p1 = points[i - 1]
            pi = points[i]
            p2 = points[i + 1]
            area = calculate_area(p1, pi, p2)
            if area < min_area:
                min_area = area
                remove_index = i
            elif area == min_area and pi[0] < points[remove_index][0]:
                remove_index = i
        points.pop(remove_index)
        n -= 1
    return points

def main():
    input_data = sys.stdin.read().splitlines()
    n, m = map(int, input_data[0].split())
    points = [tuple(map(int, line.split())) for line in input_data[1:]]
    simplified_points = simplify_polyline(list(points), m)
    for i in range(m - 1):
        print(simplified_points.index(points[i + 1]) + 1)

if __name__ == "__main__":
    main()