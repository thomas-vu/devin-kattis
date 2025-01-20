import math

def calculate_fence_length(area):
    side = math.sqrt(area)
    fence_length = 4 * side
    return fence_length

# Read the input area from the user
area = float(input())

# Calculate and output the fence length
fence_length = calculate_fence_length(area)
print("{:.10f}".format(fence_length))