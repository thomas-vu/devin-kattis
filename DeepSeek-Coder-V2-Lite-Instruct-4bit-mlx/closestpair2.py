import sys
import math

def closest_pair(points):
    if len(points) <= 3:
        min_dist = float('inf')
        closest_pair = ()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
                if dist < min_dist:
                    min_dist = dist
                    closest_pair = (points[i], points[j])
        return closest_pair
    
    mid = len(points) // 2
    mid_point = points[mid]
    
    left_points = points[:mid]
    right_points = points[mid:]
    
    left_closest = closest_pair(left_points)
    right_closest = closest_pair(right_points)
    
    min_dist = min(math.sqrt((left_closest[0][0] - left_closest[1][0])**2 + (left_closest[0][1] - left_closest[1][1])**2),
                   math.sqrt((right_closest[0][0] - right_closest[1][0])**2 + (right_closest[0][1] - right_closest[1][1])**2))
    
    strip = [point for point in points if abs(point[0] - mid_point[0]) < min_dist]
    strip.sort(key=lambda point: point[1])
    
    min_strip_dist = float('inf')
    closest_pair_strip = ()
    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if (strip[j][1] - strip[i][1])**2 >= min_dist:
                break
            dist = math.sqrt((strip[i][0] - strip[j][0])**2 + (strip[i][1] - strip[j][1])**2)
            if dist < min_strip_dist:
                min_strip_dist = dist
                closest_pair_strip = (strip[i], strip[j])
    
    return min(left_closest, right_closest, key=lambda pair: math.sqrt((pair[0][0] - pair[1][0])**2 + (pair[0][1] - pair[1][1])**2)) if min_dist != float('inf') else closest_pair_strip

def main():
    while True:
        n = int(input().strip())
        if n == 0:
            break
        points = [tuple(map(float, input().strip().split())) for _ in range(n)]
        points.sort()
        closest = closest_pair(points)
        print("{:.2f} {:.2f} {:.2f} {:.2f}".format(closest[0][0], closest[0][1], closest[1][0], closest[1][1]))

if __name__ == "__main__":
    main()