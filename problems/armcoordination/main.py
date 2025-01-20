x, y = map(int, input().split())
r = int(input())

# Calculate the side length of the square
side_length = 2 * r

# Coordinates of the bottom left corner of the square
bottom_left = (x - r, y - r)
top_right = (x + r, y + r)

# Output the coordinates of the corners in clockwise order
print(bottom_left[0], bottom_left[1])
print(top_right[0], top_right[1])
print(bottom_left[0], top_right[1])
print(top_right[0], bottom_left[1])