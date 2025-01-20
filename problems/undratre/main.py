import sys

# Read input from stdin
n, k = map(int, sys.stdin.readline().strip().split())

# Calculate the minimum and maximum height of the wondertree
min_height = 1
max_height = 1

# Calculate the minimum and maximum width of the wondertree
min_width = 1
max_width = 1

# Update the height and width based on the number of days and watering constraints
for day in range(n):
    if min_width == 1:
        # If the tree has only one leaf, it can grow up to n+1 branches in height
        min_height = max(min_height, day + 2)
    else:
        # If the tree has more than one leaf, it can grow up to n+1 branches in height
        min_height = max(min_height, day + 2)
    
    # The width can grow up to k*day + 1 leaves if watered less than k times
    min_width = max(min_width, day + 1)
    if day < n - 1:
        max_width = min(max_width, k * (day + 1) + 1)
    else:
        # After n days, the width can grow up to k*n + 1 leaves
        max_width = min(max_width, k * n + 1)

# Output the results
print(min_height, max_height)
print(min_width, max_width)