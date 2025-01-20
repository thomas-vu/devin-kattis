import sys

def area_of_triangle(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2.0)

def is_point_inside(x1, y1, x2, y2, x3, y3, px, py):
    area_of_full = area_of_triangle(x1, y1, x2, y2, x3, y3)
    area_a = area_of_triangle(px, py, x2, y2, x3, y3)
    area_b = area_of_triangle(x1, y1, px, py, x3, y3)
    area_c = area_of_triangle(x1, y1, x2, y2, px, py)
    if area_of_full == area_a + area_b + area_c:
        return True
    else:
        return False

# Read the vertices of the triangle
x1, y1 = map(int, sys.stdin.readline().split())
x2, y2 = map(int, sys.stdin.readline().split())
x3, y3 = map(int, sys.stdin.readline().split())

# Read the number of apple trees
N = int(sys.stdin.readline().strip())

# Read the coordinates of all apple trees
trees = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# Calculate the area of the triangle
area = area_of_triangle(x1, y1, x2, y2, x3, y3)

# Count the number of trees inside or on the border of the triangle
count = 0
for tree in trees:
    if is_point_inside(x1, y1, x2, y2, x3, y3, *tree):
        count += 1

# Output the area and the number of trees
print("{:.1f}".format(area))
print(count)