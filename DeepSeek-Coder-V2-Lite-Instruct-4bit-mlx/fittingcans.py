def min_area(n, heights):
    max_height = max(heights)
    min_area = float('inf')
    
    for height in range(1, max_height + 1):
        width = sum((height if h >= height else (h // (2 * height) + (1 if h % (2 * height) > 0 else 0))) for h in heights)
        area = width * height
        min_area = min(min_area, area)
    
    return min_area * 66

# Read input
n = int(input())
heights = list(map(int, input().split()))

# Calculate and print the result
print(min_area(n, heights))