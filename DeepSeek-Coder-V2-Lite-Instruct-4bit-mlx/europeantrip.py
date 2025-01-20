import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def centroid(x1, y1, x2, y2, x3, y3):
    return ((x1 + x2 + x3) / 3.0, (y1 + y2 + y3) / 3.0)

# Read input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# Calculate centroid of the three points
cx, cy = centroid(x1, y1, x2, y2, x3, y3)

# Output the centroid as the optimal position for Ms. Mask's house
print(f"{cx:.10f} {cy:.10f}")