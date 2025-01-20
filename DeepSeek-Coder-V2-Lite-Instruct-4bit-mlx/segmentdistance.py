import math

def distance_point_to_segment(px, py, x1, y1, x2, y2):
    # Calculate the perpendicular distance from point (px, py) to the line segment defined by (x1, y1) and (x2, y2)
    # Using the formula: https://en.wikipedia.org/wiki/Distance_from_a_point_to_a_line
    numerator = abs((x2 - x1) * (y1 - py) - (x1 - px) * (y2 - y1))
    denominator = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return numerator / denominator

def closest_distance_segments(x1, y1, x2, y2, x3, y3, x4, y4):
    # Check if the segments are parallel or coincident and calculate distance accordingly
    p = (x4 - x3) * (y2 - y1) - (y4 - y3) * (x2 - x1)
    
    if p == 0:
        # The segments are parallel or coincident, calculate the minimum distance between any point on one segment and another segment
        min_dist = float('inf')
        points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
                min_dist = min(min_dist, dist)
        return round(min_dist, 2)
    else:
        # Use the general formula for the distance between two skew lines in 3D space and project them to 2D
        ux, uy = (x2 - x1), (y2 - y1)
        vx, vy = (x4 - x3), (y4 - y3)
        wx, wy = (x1 - x3), (y1 - y3)
        
        d = ux * vy - uz * vx
        if d == 0:
            # The lines are parallel, use the distance between a point on one line and the other line
            min_dist = float('inf')
            points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
            for i in range(len(points)):
                dist = distance_point_to_segment(points[i][0], points[i][1], x3, y3, x4, y4)
                min_dist = min(min_dist, dist)
            return round(min_dist, 2)
        else:
            # Calculate the distance between two skew lines using the formula
            c1 = (ux * wx + uy * wy) / d**2
            c2 = (vx * wx + vy * wy) / d**2
            px, py = x1 + c1 * ux, y1 + c1 * uy
            qx, qy = x3 + c2 * vx, y3 + c2 * vy
            return round(math.sqrt((px - qx)**2 + (py - qy)**2), 2)

def main():
    n = int(input())
    for _ in range(n):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
        print("{:.2f}".format(closest_distance_segments(x1, y1, x2, y2, x3, y3, x4, y4)))

if __name__ == "__main__":
    main()