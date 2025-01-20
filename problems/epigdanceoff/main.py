def dance_rating(N, M, grid):
    rating = 0
    for col in range(M):
        if all(grid[row][col] == '$' for row in range(N)):
            rating += 1
    return rating

# Read input
import sys
input = sys.stdin.read
data = input().split()
N, M = int(data[0]), int(data[1])
grid = data[2:]

# Calculate and output the rating
print(dance_rating(N, M, grid))