def calculate_other_endpoint(x1, y1):
    # The pool is an isosceles right triangle with legs of length 250
    # The coordinates of the pool's vertices are: (0, 0), (250, 0), and (0, 250)
    
    # Determine the coordinates of the other endpoint based on the given endpoint
    if x1 == 0 and y1 == 0:
        # The given endpoint is (0, 0)
        # The line divides the pool into two equal areas
        # The other endpoint will be on the edge y = x, since the pool is symmetric about this line
        # The length of the segment from (0, 0) to the other endpoint is sqrt(250^2 + 250^2) = 250*sqrt(2)
        x2 = y2 = 250 / (1 + sqrt(2))
    elif x1 == 250 and y1 == 0:
        # The given endpoint is (250, 0)
        # The line divides the pool into two equal areas
        # The other endpoint will be on the edge y = 250 - x, since the pool is symmetric about this line
        # The length of the segment from (250, 0) to the other endpoint is sqrt(250^2 + 250^2) = 250*sqrt(2)
        x2 = y2 = 250 - (250 / (1 + sqrt(2)))
    elif x1 == 0 and y1 == 250:
        # The given endpoint is (0, 250)
        # The line divides the pool into two equal areas
        # The other endpoint will be on the edge x = 250 - y, since the pool is symmetric about this line
        # The length of the segment from (0, 250) to the other endpoint is sqrt(250^2 + 250^2) = 250*sqrt(2)
        x2 = 250 - (250 / (1 + sqrt(2)))
        y2 = 250 / (1 + sqrt(2))
    else:
        # The given endpoint is on the edge of the pool
        # Calculate the other endpoint based on symmetry and equal area division
        if x1 == 0:
            # The given endpoint is on the y-axis
            x2 = y1
            y2 = 0
        elif y1 == 0:
            # The given endpoint is on the x-axis
            x2 = 0
            y2 = x1
        elif x1 == 250:
            # The given endpoint is on the right edge of the pool
            x2 = 250 - y1
            y2 = 250
        elif y1 == 250:
            # The given endpoint is on the top edge of the pool
            x2 = 250
            y2 = 250 - x1
    
    # Round the coordinates to two decimal places
    return (round(x2, 2), round(y2, 2))

# Example usage:
x1, y1 = map(int, input().split())
result = calculate_other_endpoint(x1, y1)
print("{:.2f} {:.2f}".format(*result))