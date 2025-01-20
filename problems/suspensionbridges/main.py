import math

def length_of_cable(d, s):
    a = (d / 2) * math.cosh((d / (2 * a)) - s)
    return 2 * a * math.sinh(d / (2 * a))

# Read input
d, s = map(int, input().split())

# Calculate the parameter a
a = (d / 2) * math.cosh((d / (2 * a)) - s)

# Calculate the length of the cable
cable_length = 2 * a * math.sinh(d / (2 * a))

# Output the result within the required precision
print("{:.8f}".format(cable_length))