import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def scale_factor(r, points):
    # Calculate the perimeter of the original polygon
    perimeter = 0
    for i in range(len(points)):
        next_index = (i + 1) % len(points)
        perimeter += distance(*points[i], *points[next_index])
    
    # Calculate the centroid of the original polygon
    centroid_x = sum(point[0] for point in points) / len(points)
    centroid_y = sum(point[1] for point in points) / len(points)
    
    # Calculate the distance from centroid to each vertex
    max_distance = 0
    for point in points:
        dist = distance(centroid_x, centroid_y, *point)
        if dist > max_distance:
            max_distance = dist
    
    # Check if the minimum radius can be achieved by scaling down
    if max_distance < r:
        return "Not possible"
    
    # Calculate the scaling factor
    scale_factor = r / max_distance
    
    # Check if the scaled perimeter matches the original length
    scaled_perimeter = 0
    for i in range(len(points)):
        next_index = (i + 1) % len(points)
        x1, y1 = points[i]
        x2, y2 = points[next_index]
        scaled_x1 = centroid_x + scale_factor * (x1 - centroid_x)
        scaled_y1 = centroid_y + scale_factor * (y1 - centroid_y)
        scaled_x2 = centroid_x + scale_factor * (x2 - centroid_x)
        scaled_y2 = centroid_y + scale_factor * (y2 - centroid_y)
        scaled_perimeter += distance(scaled_x1, scaled_y1, scaled_x2, scaled_y2)
    
    # Check if the relative error is within 10^-5
    if abs(scaled_perimeter - perimeter) / perimeter < 1e-5:
        return scale_factor
    else:
        return "Not possible"

# Read number of test cases
t = int(input())
for _ in range(t):
    r, n = map(int, input().split())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    result = scale_factor(r, points)
    print("{:.5f}".format(result) if isinstance(result, float) else result)