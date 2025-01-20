def min_additional_lines(x1, y1, x2, y2):
    # Determine the minimum number of additional line segments needed
    if x1 == x2:  # Vertical line segment
        return 1
    elif y1 == y2:  # Horizontal line segment
        return 1
    else:  # Diagonal line segment
        return 2

# Read input from stdin
x1, y1, x2, y2 = map(int, input().split())

# Output the result
print(min_additional_lines(x1, y1, x2, y2))