def find_fourth_vertex(points):
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    
    x4 = (set(x_coords) - set([p[0] for p in points])).pop()
    y4 = (set(y_coords) - set([p[1] for p in points])).pop()
    
    return x4, y4

# Read input
points = []
for _ in range(3):
    x, y = map(int, input().split())
    points.append((x, y))

# Find and print the fourth vertex
fourth_vertex = find_fourth_vertex(points)
print(*fourth_vertex)