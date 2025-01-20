import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
heights = [int(input()) for _ in range(N)]
# Find the index of the highest block
max_height = max(heights)
highest_index = heights.index(max_height)

# Initialize the jump count list with a large number, except for the highest block which is 0
jumps = [float('inf')] * N
for i in range(N):
    if heights[i] == max_height:
        jumps[i] = 0

# Traverse from the highest block to left
for i in range(highest_index - 1, -1, -1):
    if heights[i] < heights[i + 1]:
        jumps[i] = min(jumps[i], jumps[i + 1] + 1)

# Traverse from the highest block to right
for i in range(highest_index + 1, N):
    if heights[i] < heights[i - 1]:
        jumps[i] = min(jumps[i], jumps[i - 1] + 1)

# Output the result
print(' '.join(map(str, jumps)))