import math

def min_distance(x, y, x1, y1, x2, y2):
    # Calculate the distances to each corner of the house
    dist_top_left = math.sqrt((x - x1)**2 + (y - y2)**2)
    dist_top_right = math.sqrt((x - x2)**2 + (y - y2)**2)
    dist_bottom_left = math.sqrt((x - x1)**2 + (y - y1)**2)
    dist_bottom_right = math.sqrt((x - x2)**2 + (y - y1)**2)
    
    # Calculate the minimum distance to avoid the house
    min_dist = float('inf')
    if x < x1:
        # Goat is to the left of the house
        min_dist = min(min_dist, dist_top_left, dist_bottom_left)
    elif x > x2:
        # Goat is to the right of the house
        min_dist = min(min_dist, dist_top_right, dist_bottom_right)
    if y < y1:
        # Goat is below the house
        min_dist = min(min_dist, dist_bottom_left, dist_bottom_right)
    elif y > y2:
        # Goat is above the house
        min_dist = min(min_dist, dist_top_left, dist_top_right)
    else:
        # Goat is inside the house (shouldn't happen as per problem statement)
        min_dist = min(min_dist, dist_top_left, dist_top_right, dist_bottom_left, dist_bottom_right)
    
    # Calculate the distance to the nearest edge of the house
    dist_to_left = abs(x - x1)
    dist_to_right = abs(x - x2)
    dist_to_bottom = abs(y - y1)
    dist_to_top = abs(y - y2)
    
    # Use the minimum distance to an edge plus the radius of the goat's tether rope
    min_dist = min(min_dist, dist_to_left, dist_to_right, dist_to_bottom, dist_to_top)
    
    return min_dist

# Read input
x, y = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# Calculate and print the result with a precision of 0.001
result = min_distance(x, y, x1, y1, x2, y2)
print("{:.3f}".format(result))