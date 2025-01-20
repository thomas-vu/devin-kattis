import sys
import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_pair(points):
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    
    return closest_pair

def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        
        points = []
        for _ in range(n):
            x, y = map(float, sys.stdin.readline().strip().split())
            points.append((x, y))
        
        pair = closest_pair(points)
        print("{:.2f} {:.2f} {:.2f} {:.2f}".format(pair[0][0], pair[0][1], pair[1][0], pair[1][1]))

if __name__ == "__main__":
    main()