import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    C = int(input())
    if C < 2:
        return
    
    points = []
    for _ in range(C):
        x, y = map(int, input().split())
        points.append((x, y))
    
    max_distance = 0
    for i in range(C):
        for j in range(i+1, C):
            distance = calculate_distance(points[i][0], points[i][1], points[j][0], points[j][1])
            if distance > max_distance:
                max_distance = distance
    
    print("{:.10f}".format(max_distance))

if __name__ == "__main__":
    main()