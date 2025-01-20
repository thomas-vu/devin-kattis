import sys
from itertools import combinations

def distance_squared(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def count_segments(points):
    n = len(points)
    count = 0
    for (i, j) in combinations(range(n), 2):
        if distance_squared(*points[i], *points[j]) == 2018**2:
            count += 1
    return count

# Read input
n = int(sys.stdin.readline().strip())
points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Count and output the number of segments
result = count_segments(points)
print(result)