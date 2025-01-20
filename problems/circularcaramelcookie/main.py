import math

def min_radius(s):
    # The minimum radius is the side length of a square with more than s squares
    min_side = math.sqrt(s + 1)
    
    # The radius of the stroopwafel is half the side length of the square with more than s squares
    min_radius = math.sqrt(2) * (min_side / 2)
    
    return min_radius

# Read the input
s = int(input().strip())

# Calculate and output the minimum radius
print("{:.10f}".format(min_radius(s)))