import sys
from itertools import combinations

def distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

def area_of_triangle(p1, p2, p3):
    a = distance(p1, p2)
    b = distance(p2, p3)
    c = distance(p1, p3)
    s = (a + b + c) / 2
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5

def main():
    N = int(sys.stdin.readline().strip())
    points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
    
    max_area = 0.0
    for p1, p2, p3 in combinations(points, 3):
        area = area_of_triangle(p1, p2, p3)
        max_area = max(max_area, area)
    
    print("{:.4f}".format(max_area))

if __name__ == "__main__":
    main()