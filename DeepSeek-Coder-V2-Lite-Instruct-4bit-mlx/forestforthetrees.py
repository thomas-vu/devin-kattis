x_b, y_b = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())

# Check if there is a tree blocking the line of sight to Belle
def can_see_belle(x_b, y_b, x1, y1, x2, y2):
    # Check if Belle is inside the rectangle
    if (x1 <= x_b <= x2 and y1 <= y_b <= y2):
        return "No", (x_b, y_b)
    
    # Check if there is a tree on the boundary of the rectangle blocking the view
    if (x_b == x1 or x_b == x2 or y_b == y1 or y_b == y2):
        return "No", (x1, y_b) if x_b == x1 or x_b == x2 else ("No", (x_b, y1)) if y_b == y1 or y_b == y2 else ("No", (x_b, y2))
    
    # Check if there is a tree blocking the view in the rectangle
    for x in range(x1, x2 + 1):
        if (x == x_b and y1 <= y_b <= y2) or (y_b == y1 and x1 <= x_b <= x2):
            return "No", (x, y_b) if x == x_b else ("No", (x_b, y1))
    for y in range(y1, y2 + 1):
        if (y == y_b and x1 <= x_b <= x2) or (x_b == x1 and y1 <= y_b <= y2):
            return "No", (x_b, y) if y == y_b else ("No", (x1, y_b))
    
    return "Yes"

result = can_see_belle(x_b, y_b, x1, y1, x2, y2)
if result == "Yes":
    print("Yes")
else:
    print("No", result[1][0], result[1][1])