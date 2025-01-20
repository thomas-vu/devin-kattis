def calculate_triangle_area(height, base):
    area = (height * base) / 2.0
    return area

# Read input
h, b = map(int, input().split())

# Calculate and output the area
area = calculate_triangle_area(h, b)
print("{:.7f}".format(area))