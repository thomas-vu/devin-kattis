import sys
import random
from math import sqrt, atan2, pi

# Constants
g = 10.0

def calculate_intersection(x, y, v, k):
    # Calculate the time when the kunai hits the ground
    t = (2 * y + g * x**2) / (2 * v**2)
    return t

def is_hit(x, y, bottom_poly, top_poly):
    n = len(bottom_poly)
    m = len(top_poly)
    
    for i in range(n):
        j = (i + 1) % n
        if bottom_poly[i][0] == bottom_poly[j][0]:  # Vertical line
            for k in range(m):
                l = (k + 1) % m
                if top_poly[k][0] == top_poly[l][0]:  # Vertical line
                    continue
                if min(bottom_poly[i][1], bottom_poly[j][1]) <= y + g * x**2 / (2 * v**2) <= max(bottom_poly[i][1], bottom_poly[j][1]) and \
                   min(top_poly[k][1], top_poly[l][1]) <= y + g * x**2 / (2 * v**2) <= max(top_poly[k][1], top_poly[l][1]):
                    return True
                # Check intersection of line segments (x, y) to (x + v * t, y - g * t**2 / 2) with the top and bottom edges
                a1, b1 = (bottom_poly[i][0], bottom_poly[i][1]), (bottom_poly[j][0], bottom_poly[j][1])
                a2, b2 = (top_poly[k][0], top_poly[k][1]), (top_poly[l][0], top_poly[l][1])
                if intersect(a1, b1, a2, b2):
                    return True
        else:  # Horizontal line
            for k in range(m):
                l = (k + 1) % m
                if top_poly[k][0] == top_poly[l][0]:  # Vertical line
                    continue
                if min(bottom_poly[i][0], bottom_poly[j][0]) <= x + v * t <= max(bottom_poly[i][0], bottom_poly[j][0]) and \
                   min(top_poly[k][1], top_poly[l][1]) <= y + g * t**2 / 2 <= max(top_poly[k][1], top_poly[l][1]):
                    return True
                # Check intersection of line segments (x, y) to (x + v * t, y - g * t**2 / 2) with the top and bottom edges
                a1, b1 = (bottom_poly[i][0], bottom_poly[i][1]), (bottom_poly[j][0], bottom_poly[j][1])
                a2, b2 = (top_poly[k][0], top_poly[k][1]), (top_poly[l][0], top_poly[l][1])
                if intersect(a1, b1, a2, b2):
                    return True
    return False

def intersect(a1, b1, a2, b2):
    def ccw(A, B, C):
        return (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0])
    return ccw(a1, b2, a2) != ccw(b1, b2, a2) and ccw(a1, b1, a2) != ccw(b1, b2, a2)

def calculate_probability(w, h, bottom_poly, top_poly, k, L, R):
    successful_throws = 0
    total_throws = 100000
    
    for _ in range(total_throws):
        v = random.uniform(L, R)
        t = calculate_intersection(w, k, v, g)
        if not is_hit(w, h, bottom_poly, top_poly):
            successful_throws += 1
    
    return successful_throws / total_throws

# Read input from stdin
input_lines = sys.stdin.read().splitlines()
C = int(input_lines[0])
case_idx = 1

for _ in range(C):
    w, h, nb, nt = map(int, input_lines[case_idx].split())
    case_idx += 1
    bottom_poly = [tuple(map(int, input_lines[case_idx].split())) for _ in range(nb)]
    case_idx += 1
    top_poly = [tuple(map(int, input_lines[case_idx].split())) for _ in range(nt)]
    case_idx += 1
    k, L, R = map(int, input_lines[case_idx].split())
    case_idx += 1
    
    probability = calculate_probability(w, h, bottom_poly, top_poly, k, L, R)
    print("{:.10f}".format(probability))