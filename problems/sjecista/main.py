def count_diagonal_intersections(N):
    # The number of intersections between diagonals in a convex polygon with N vertices is given by the formula:
    # (N * (N - 1) * (N - 2) * (N - 3)) // 8
    # This is because for each pair of diagonals, there are N - 3 points where they can intersect inside the polygon.
    return (N * (N - 1) * (N - 2) * (N - 3)) // 8

# Read the number of vertices from input
N = int(input().strip())

# Output the result
print(count_diagonal_intersections(N))