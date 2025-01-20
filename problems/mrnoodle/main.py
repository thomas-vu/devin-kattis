import sys
from math import sqrt, cos, pi

def minimum_radius(N, sides):
    # Calculate the perimeter of the polygon
    total_length = sum(sides)
    
    # Use the Law of Cosines to find the minimum angle in the polygon
    min_angle = float('inf')
    for i in range(N):
        j = (i + 1) % N
        k = (i + 2) % N
        a, b, c = sides[i], sides[j], sides[k]
        angle = acos((a**2 + b**2 - c**2) / (2.0 * a * b))
        min_angle = min(min_angle, angle)
    
    # The minimum radius is half the longest side divided by sin of the smallest angle
    max_side = max(sides)
    min_sin_angle = sin(min_angle / 2.0)
    
    # The minimum radius of the circle that can fit the polygon is half the longest side divided by sin of half the smallest angle
    r = max_side / (2.0 * min_sin_angle)
    
    return r

# Read input from stdin
N = int(sys.stdin.readline().strip())
sides = list(map(int, sys.stdin.readline().strip().split()))

# Calculate and print the result
r = minimum_radius(N, sides)
print("{:.10f}".format(r))