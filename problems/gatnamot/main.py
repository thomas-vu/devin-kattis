import math

def count_intersections(r):
    # The number of intersections within the circle is determined by counting the points (x, y)
    # where x^2 + y^2 <= r^2. This is a quarter circle in the first quadrant, so we multiply by 4
    # and add the points on the axes.
    
    count = 0
    for x in range(int(math.ceil(r**0.5))):
        y = math.sqrt(r - x*x)  # Use the Pythagorean theorem to find y
        if y.is_integer():
            count += 1
    count = int(count * 4) + (4*r//1) + 1  # Add the points on the axes and the quarter circle
    return count

# Read input
r = int(input().strip())

# Output the result
print(count_intersections(r))