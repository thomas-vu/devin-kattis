# This solution assumes that the given points form a right triangle with one side on the x-axis and one side on the y-axis
# It calculates the missing corner by using the coordinates of the other three corners

def find_fourth_corner(points):
    # Sort points by x and y to determine the right triangle's sides
    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
    
    # The right triangle's sides are the differences in x and y between adjacent points
    dx1 = sorted_points[1][0] - sorted_points[0][0]
    dy1 = sorted_points[1][1] - sorted_points[0][1]
    dx2 = sorted_points[2][0] - sorted_points[1][0]
    dy2 = sorted_points[2][1] - sorted_points[1][1]
    
    # The fourth corner is calculated by adding the differences to one of the points
    x4 = sorted_points[2][0] + dx1
    y4 = sorted_points[2][1] + dy1
    
    return (x4, y4)

# Read input from stdin
points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

# Get the fourth corner coordinates
fourth_corner = find_fourth_corner(points)

# Output the result
print(*fourth_corner)