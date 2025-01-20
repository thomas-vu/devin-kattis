import math

def distance(ax, ay, bx, by, M, N, R):
    # Convert the points to polar coordinates
    a_theta = (ax / float(M)) * 2 * math.pi
    b_theta = (bx / float(M)) * 2 * math.pi
    a_rho = (ay + 1) / float(N + 1) * R
    b_rho = (by + 1) / float(N + 1) * R
    
    # Calculate the Euclidean distance in polar coordinates
    x = (b_rho * math.cos(b_theta) - a_rho * math.cos(a_theta)) ** 2
    y = (b_rho * math.sin(b_theta) - a_rho * math.sin(a_theta)) ** 2
    z = (b_rho - a_rho) ** 2
    
    # Pythagorean theorem for the distance on the surface of a sphere
    return math.sqrt(x + y - z) if x + y > z else 0

# Read input
M, N, R = map(float, input().split())
ax, ay, bx, by = map(int, input().split())

# Calculate the distance and output it
result = distance(ax, ay, bx, by, int(M), int(N), R)
print("{:.15f}".format(result))