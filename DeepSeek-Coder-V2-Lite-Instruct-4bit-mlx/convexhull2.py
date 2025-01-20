import sys
from math import atan2, pi

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def angle_cmp(a, b):
    ang_a = atan2(a[1], a[0])
    ang_b = atan2(b[1], b[0])
    if ang_a != ang_b:
        return (ang_a < ang_b) - (ang_a > ang_b)
    if a[1] != b[1]:
        return (a[1] < b[1]) - (a[1] > b[1])
    return (a[0] < b[0]) - (a[0] > b[0])

def main():
    n = int(sys.stdin.readline().strip())
    points = [read_ints() for _ in range(n)]
    
    # Filter out points not on the hull
    hull_points = [p for p in points if p[2] == 'Y']
    
    # Sort the hull points by angle from the first point in the hull
    start_point = min(hull_points, key=lambda p: (p[0], p[1]))
    hull_points.remove(start_point)
    sorted_hull = [start_point] + sorted(hull_points, key=lambda p: angle_cmp((p[0] - start_point[0], p[1] - start_point[1]), (0, 1)))
    
    # Output the result
    print(len(sorted_hull))
    for point in sorted_hull:
        print(f"{point[0]} {point[1]}")

if __name__ == "__main__":
    main()