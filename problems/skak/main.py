def min_moves(xh, yh, xp, yp):
    # The minimum number of moves is the maximum distance in either x or y direction
    return max(abs(xh - xp), abs(yh - yp))

# Read input
xh, yh = map(int, input().split())
xp, yp = map(int, input().split())

# Calculate and print the minimum number of moves
print(min_moves(xh, yh, xp, yp))