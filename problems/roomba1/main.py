import sys
from math import sqrt, ceil

def min_path(r, d):
    # The robot can vacuum the entire room starting from (0, 0) and returning to (0, 0)
    # The robot can move in a grid of r rows and d columns
    # The minimum path is the sum of the number of moves in both dimensions
    return r + d - 2

# Read input from stdin
input_line = sys.stdin.readline().strip()
r, d = map(int, input_line.split())

# Calculate the minimum path length
result = min_path(r, d)

# Output the result
print(result)