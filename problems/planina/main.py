def count_points(N):
    points = 1
    for _ in range(N):
        points = (points * 4) - 4 + 1
    return points

# Read input from stdin
N = int(input().strip())
print(count_points(N))