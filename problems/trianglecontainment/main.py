import sys
from itertools import combinations

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())
treasures = []
for _ in range(n):
    x_val, y_val, v = map(int, sys.stdin.readline().split())
    treasures.append((x_val, y_val, v))

# Function to calculate the sum of values inside a triangle
def enclosed_value(a, b, c):
    total_value = 0
    for treasure in treasures:
        if not is_inside(a, b, c, treasure):
            continue
        total_value += treasure[2]
    return total_value

# Function to check if a point is inside a triangle
def is_inside(a, b, c, pt):
    d = sign(pt, a, b) + sign(pt, b, c) + sign(pt, c, a)
    return d == 3 or d == -3

# Helper function to determine sign of area
def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

# Calculate and output the result for each treasure point
for i in range(n):
    a = (0, 0)
    b = (x, 0)
    c = treasures[i][:2]
    total_value = enclosed_value(a, b, c)
    print(total_value)