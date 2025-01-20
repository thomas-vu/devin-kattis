def find_square(points):
    from collections import defaultdict
    
    # Create a dictionary to count the occurrences of each pair of differences (X_diff, Y_diff)
    diff_count = defaultdict(int)
    
    # Calculate all possible differences between points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x_diff = points[i][0] - points[j][0]
            y_diff = points[i][1] - points[j][1]
            diff_count[(x_diff, y_diff)] += 1
    
    # Check for the existence of a square by finding opposite corners
    for (x_diff1, y_diff1), count in diff_count.items():
        if count < 2:
            continue
        
        # Find the pair of points that are (x_diff1, y_diff1) and (-x_diff1, -y_diff1) away from each other
        for (x_diff2, y_diff2), count in diff_count.items():
            if (x_diff1, y_diff1) == (-x_diff2, -y_diff2):
                # We have found two opposite corners of the square
                x1 = min(points[i][0] + x_diff1 for i in range(len(points)) if (x_diff1, y_diff1) == (points[i][0] - points[j][0], points[i][1] - points[j][1]))
                y1 = min(points[i][1] + y_diff1 for i in range(len(points)) if (x_diff1, y_diff1) == (points[i][0] - points[j][0], points[i][1] - points[j][1]))
                x2 = min(points[i][0] + x_diff2 for i in range(len(points)) if (x_diff2, y_diff2) == (points[i][0] - points[j][0], points[i][1] - points[j][1]))
                y2 = min(points[i][1] + y_diff2 for i in range(len(points)) if (x_diff2, y_diff2) == (points[i][0] - points[j][0], points[i][1] - points[j][1]))
                return f"{x1} {x2} {y1} {y2}"
    
    return "Impossible"

# Read input
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Find and print the result
print(find_square(points))