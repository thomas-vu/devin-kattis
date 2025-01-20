import math

# Function to calculate the distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate the length of the unlock pattern
def calc_length(pattern):
    # Define the positions of each pivot on a unit grid
    pivots = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2)
    }
    
    length = 0.0
    prev_pivot = None
    
    for pivot in pattern:
        if prev_pivot is not None:
            length += distance(pivots[prev_pivot][0], pivots[prev_pivot][1], pivots[pivot][0], pivots[pivot][1])
        prev_pivot = pivot
    
    return length

# Read the input pattern
pattern = []
for _ in range(3):
    line = list(map(int, input().split()))
    pattern.extend(line)

# Calculate and output the length of the unlock pattern
length = calc_length(pattern)
print("{:.10f}".format(length))