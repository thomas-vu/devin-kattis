def maximum_possible_difference(N, heights):
    # Sort the heights to maximize the difference between adjacent elements
    sorted_heights = sorted(heights)
    
    # The maximum difference will be between the smallest and largest elements
    max_diff = sorted_heights[-1] - sorted_heights[0]
    
    return max_diff

# Read input
N = int(input().strip())
heights = list(map(int, input().strip().split()))

# Calculate and output the result
result = maximum_possible_difference(N, heights)
print(result)