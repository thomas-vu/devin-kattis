import sys
from math import sqrt, inf

def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def can_place(blueberry, redberry, min_dist):
    for b in blueberry:
        for r in redberry:
            if distance(b, r) >= min_dist:
                return True
    return False

def find_max_min_distance(N, B, R, blueberry, redberry):
    left, right = 0.0, max(max([b[0] for b in blueberry], [r[0] for r in redberry]) - min([b[0] for b in blueberry], [r[0] for r in redberry]),
                            max([b[1] for b in blueberry], [r[1] for r in redberry]) - min([b[1] for b in blueberry], [r[1] for r in redberry]))
                            ) + 1.0
    while right - left > 1e-6:
        mid = (left + right) / 2.0
        if can_place(blueberry, redberry, mid):
            left = mid
        else:
            right = mid
    return left

# Read input
N, B, R = map(int, sys.stdin.readline().strip().split())
blueberry = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(B)]
redberry = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(R)]

# Calculate and output the result
result = find_max_min_distance(N, B, R, blueberry, redberry)
print("{:.12f}".format(result))