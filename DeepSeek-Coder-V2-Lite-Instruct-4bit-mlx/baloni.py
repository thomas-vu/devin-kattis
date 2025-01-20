def min_arrows(N, heights):
    arrows = 0
    while len(heights) > 0:
        min_height = min(heights)
        arrows += 1
        heights = [h - 1 for h in heights if h > min_height]
    return arrows

# Read input from stdin
N = int(input().strip())
heights = list(map(int, input().strip().split()))

# Output the result
print(min_arrows(N, heights))