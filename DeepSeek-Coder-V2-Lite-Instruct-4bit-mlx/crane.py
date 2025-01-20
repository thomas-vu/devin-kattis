import sys
from itertools import combinations

def sign(x):
    return (x > 0) - (x < 0)

def cross(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]

def left_turn(p1, p2, p3):
    return sign(cross((p2[0] - p1[0], p2[1] - p1[1]), (p3[0] - p2[0], p3[1] - p2[1]))) > 0

def toppling_range(points):
    n = len(points)
    min_weight = float('inf')
    max_weight = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if points[i][1] == 0 and points[j][1] == 0:
                continue
            left_sum = right_sum = 0
            for k in range(n):
                if left_turn(points[i], points[j], points[k]):
                    right_sum += points[k][1] if k != i and k != j else 0
                else:
                    left_sum += points[k][1] if k != i and k != j else 0
            min_weight = min(min_weight, max(left_sum, right_sum))
            max_weight = max(max_weight, max(left_sum, right_sum))
    
    if min_weight == float('inf'):
        return "unstable"
    elif max_weight == min_weight:
        return f"{max_weight} .. inf"
    else:
        min_w = int(min_weight)
        max_w = int(max_weight) if min_weight != max_weight else (int(max_weight) + 1)
        return f"{min_w} .. {max_w}"

# Read input
n = int(sys.stdin.readline().strip())
points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]

# Calculate and print the result
result = toppling_range(points)
print(result)