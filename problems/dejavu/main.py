def count_right_triangles(points):
    from collections import defaultdict
    
    # Counters for the number of points on the same x and y axes
    count_x = defaultdict(int)
    count_y = defaultdict(int)
    
    # Count the number of points on each x and y axis
    for x, y in points:
        count_x[x] += 1
        count_y[y] += 1
    
    # Count the number of right triangles for each x and y axis
    triangle_count = 0
    for x in count_x:
        if count_x[x] > 1:
            triangle_count += count_x[x] * (count_x[x] - 1) // 2
    for y in count_y:
        if count_y[y] > 1:
            triangle_count += count_y[y] * (count_y[y] - 1) // 2
    
    # Count the number of right triangles where points share an x or y coordinate
    for i in range(N):
        for j in range(i+1, N):
            if points[i][0] == points[j][0]:  # Same x-coordinate
                triangle_count += count_y[points[i][1]] * (count_y[points[j][1]] - 1) // 2
            elif points[i][1] == points[j][1]:  # Same y-coordinate
                triangle_count += count_x[points[i][0]] * (count_x[points[j][0]] - 1) // 2
    
    return triangle_count

# Read input
N = int(input().strip())
points = [tuple(map(int, input().strip().split())) for _ in range(N)]

# Calculate and output the result
print(count_right_triangles(points))