import math

def min_clear_area(d, x, y, h):
    # Calculate the angle in radians between the line of sight and the vertical
    angle = math.atan((x - d) / h)
    
    # Calculate the height of the clear area on the lens needed to see the entire sign
    clear_height = y / math.tan(angle) + h
    
    return clear_height

# Read input from stdin
d, x, y, h = map(int, input().split())

# Calculate and print the result
result = min_clear_area(d, x, y, h)
print("{:.6f}".format(result))