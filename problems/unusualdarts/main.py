import itertools
from typing import List, Tuple

def is_simple_polygon(points: List[Tuple[float, float]]) -> bool:
    for i in range(len(points)):
        for j in range(i + 2, len(points)):
            if i == 0 and j == len(points) - 1:
                continue
            if do_intersect(points[i], points[(i + 1) % len(points)], points[j], points[(j + 1) % len(points)]):
                return False
    return True

def do_intersect(p1, q1, p2, q2):
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    return ccw(p1, q1, p2) != ccw(p1, q1, q2) and ccw(p2, q2, p1) != ccw(p2, q2, q1)

def calculate_probability(points: List[Tuple[float, float]], bob_throws: List[Tuple[float, float]]) -> float:
    inside_count = 0
    for _ in range(10000):
        x, y = bob_throws[_ % 3]
        if is_point_in_polygon(x, y, points):
            inside_count += 1
    return inside_count / 10000

def is_point_in_polygon(x, y, polygon):
    n = len(polygon)
    inside = False
    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside

def find_order(points: List[Tuple[float, float]], p: float) -> str:
    for order in itertools.permutations(range(1, 8)):
        if is_simple_polygon([points[i - 1] for i in order]):
            bob_throws = [(0.5, 0.5), (1.5, 1.5), (1.5, 0.5)]
            if abs(calculate_probability([points[i - 1] for i in order], bob_throws) - p) < 0.0001:
                return ' '.join(map(str, order))
    return ""

def main():
    N = int(input())
    for _ in range(N):
        points = [tuple(map(float, input().split())) for _ in range(7)]
        p = float(input())
        order = find_order(points, p)
        print(order)

if __name__ == "__main__":
    main()