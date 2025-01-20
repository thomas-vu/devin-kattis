import sys

def read_ints():
    return list(map(int, input().split()))

# Read the inputs
x1, y1, x1_prime, y1_prime = read_ints()
x2, y2, x2_prime, y2_prime = read_ints()

# Calculate the differences and distances
dx1 = x1_prime - x1
dy1 = y1_prime - y1
dx2 = x2_prime - x2
dy2 = y2_prime - y2

# Check if the throws are collinear with each other
if dx1 * dy2 == dx2 * dy1:
    print(-1)
else:
    # Calculate the intersection point of the two lines
    xa = (x1 * y2_prime - y1 * x2_prime + x2 * y1_prime - y2 * x1_prime) // (dx1 * dy2 - dx2 * dy1)
    ya = (y1 * x2_prime - x1 * y2_prime + y2 * x1_prime - x2 * y1_prime) // (dx1 * dy2 - dx2 * dy1)
    print(xa, ya)