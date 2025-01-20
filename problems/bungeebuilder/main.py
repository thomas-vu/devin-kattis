def max_jumping_distance(heights):
    N = len(heights)
    max_dist = 0
    
    for i in range(N):
        for j in range(i + 1, N):
            min_height = float('inf')
            for k in range(i + 1, j):
                min_height = min(min_height, heights[k])
            if heights[i] < min_height and heights[j] < min_height:
                max_dist = max(max_dist, abs(heights[i] - heights[j]))
    
    return max_dist

# Read input
N = int(input())
heights = list(map(int, input().split()))

# Calculate and print the result
print(max_jumping_distance(heights))