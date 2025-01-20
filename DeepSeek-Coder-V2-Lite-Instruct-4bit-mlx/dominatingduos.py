def count_pairs(heights):
    n = len(heights)
    pair_count = 0
    
    for i in range(n):
        for j in range(i + 1, n):
            if all(heights[k] < heights[i] for k in range(i + 1, j)) and all(heights[k] < heights[j] for k in range(j + 1, n)):
                pair_count += 1
    
    return pair_count

# Read input
n = int(input())
heights = [int(input()) for _ in range(n)]

# Output the result
print(count_pairs(heights))