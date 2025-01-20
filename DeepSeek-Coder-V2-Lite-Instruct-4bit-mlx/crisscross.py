def count_intersection_points(n, lines):
    points = set()
    
    for i in range(n):
        x0, y0, x1, y1 = lines[i]
        for j in range(i+1, n):
            x2, y2, x3, y3 = lines[j]
            
            # Check if the lines are parallel (denominator zero case)
            denom = (x1 - x0) * (y3 - y2) - (y1 - y0) * (x3 - x2)
            if denom == 0:
                continue
            
            ua = ((x3 - x2) * (y0 - y2) - (y3 - y2) * (x0 - x2)) / denom
            ub = ((x1 - x0) * (y0 - y2) - (y1 - y0) * (x0 - x2)) / denom
            
            # Check if the intersection point is within both line segments
            if 0 <= ua <= 1 and 0 <= ub <= 1:
                points.add((x0 + ua * (x1 - x0), y0 + ua * (y1 - y0)))
    
    return len(points) if points else -1

# Read input
n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_intersection_points(n, lines))