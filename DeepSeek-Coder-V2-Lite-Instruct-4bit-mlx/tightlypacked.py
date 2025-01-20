import math

def min_empty_squares(N):
    # Calculate the minimum area of the box needed to pack N widgets
    min_area = float('inf')
    
    # Iterate through possible heights of the box
    for H in range(1, int(math.sqrt(N)) + 1):
        if N % H == 0:
            W = N // H
            # Check the valid range for width
            if H / 2 <= W <= 2 * H:
                # Calculate the total number of squares needed to pack N widgets
                total_squares = W * H
                # Calculate the number of empty squares left after packing N widgets
                empty_squares = total_squares - N
                min_area = min(min_area, empty_squares)
    
    return int(min_area)

# Read the number of widgets from input
N = int(input().strip())
print(min_empty_squares(N))