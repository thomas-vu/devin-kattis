def find_highest_peak(N, heights):
    max_height = 0
    
    for i in range(N):
        for j in range(i+1, N):
            if heights[i] <= heights[j]:
                for k in range(j+1, N):
                    if heights[j] >= heights[k]:
                        height = min(heights[j] - heights[i], heights[j] - heights[k])
                        max_height = max(max_height, height)
    
    return max_height

# Read input
N = int(input())
heights = list(map(int, input().split()))

# Find and output the highest peak height
print(find_highest_peak(N, heights))