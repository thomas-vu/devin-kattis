x_s, y_s = map(int, input().split())
x_t, y_t = map(int, input().split())
x_p, y_p = map(int, input().split())

# Calculate the number of points between start and end that avoid the swimming pool
N = 10
points = []
for i in range(N + 1):
    t = float(i / N)
    x_i = int((1 - t) * x_s + t * x_t)
    y_i = int((1 - t) * y_s + t * y_t)
    points.append((x_i, y_i))

# Output the number of points and their coordinates
print(N)
for point in points:
    print(point[0], point[1])