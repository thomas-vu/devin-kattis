import math
from itertools import combinations

def calculate_area(points):
    n = len(points)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += points[i][0] * points[j][1] - points[j][0] * points[i][1]
    return abs(area) / 2.0

def score_polygon(points, k):
    min_r = float('inf')
    max_r = 0.0
    for points_comb in combinations(points, k):
        radius = 0.0
        for point in points_comb:
            radius = max(radius, math.sqrt(point[0]**2 + point[1]**2))
        min_r = min(min_r, radius)
    for points_comb in combinations(points, k):
        radius = 0.0
        for point in points_comb:
            radius = max(radius, math.sqrt(point[0]**2 + point[1]**2))
        max_r = max(max_r, radius)
    inner_area = math.pi * min_r**2 / (4 * math.sin(2*math.pi/k))
    outer_area = math.pi * max_r**2 / (4 * math.sin(2*math.pi/k))
    return inner_area / outer_area

def main():
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    best_score = 0.0
    best_k = 3
    for k in range(3, 9):
        current_score = sum([score_polygon(points, k) for _ in range(10)]) / 10
        if current_score > best_score:
            best_score = current_score
            best_k = k
    
    print(best_k, best_score)

if __name__ == "__main__":
    main()