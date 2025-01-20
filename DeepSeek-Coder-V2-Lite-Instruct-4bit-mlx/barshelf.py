def count_messy_trios(heights):
    n = len(heights)
    count = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if heights[i] >= 2 * heights[j]:
                for k in range(j+1, n):
                    if heights[j] >= 2 * heights[k]:
                        count += 1
    return count

# Read input
n = int(input())
heights = list(map(int, input().split()))

# Calculate and output the messiness of the shelf
messy_trios = count_messy_trios(heights)
print(messy_trios)