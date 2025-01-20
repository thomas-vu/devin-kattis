import math

def calculate_angle(k, w, l):
    # Calculate the angle after k bounces
    alpha = math.atan(2 * math.tan(math.radians(l / w)))
    beta = math.degrees(alpha) * (2 ** k - 1)
    return beta

# Read input
k, w, l = map(int, input().split())

# Calculate and print the output
beta = calculate_angle(k, w, l)
print("{:.8f}".format(beta))