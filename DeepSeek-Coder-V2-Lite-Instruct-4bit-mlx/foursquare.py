def can_form_square(widths, heights):
    # Sort the widths and heights to find the smallest and largest dimensions
    sorted_widths = sorted(widths)
    sorted_heights = sorted(heights)
    
    # Check if the smallest and largest dimensions can form a square
    side = max(sorted_widths[3], sorted_heights[3])
    
    # Check if the remaining two dimensions can fit within the square formed by the largest dimension
    return 1 if sorted_widths[2] + sorted_heights[2] == side else 0

# Read input
widths = []
heights = []
for _ in range(4):
    w, h = map(int, input().split())
    widths.append(w)
    heights.append(h)

# Check if the panes can form a square and output the result
print(can_form_square(widths, heights))