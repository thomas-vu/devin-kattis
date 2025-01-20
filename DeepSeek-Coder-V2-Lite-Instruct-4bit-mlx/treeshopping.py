def min_height_difference(n, k, heights):
    min_diff = float('inf')
    for i in range(n - k + 1):
        subrange_heights = heights[i:i+k]
        min_diff = min(min_diff, max(subrange_heights) - min(subrange_heights))
    return min_diff

# Read input
n, k = map(int, input().split())
heights = list(map(int, input().split()))

# Calculate and output the result
result = min_height_difference(n, k, heights)
print(result)