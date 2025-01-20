import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area_polygon(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

while True:
    n = int(input())
    if n == 0:
        break
    
    beacons = []
    for _ in range(n):
        x, y = map(int, input().split())
        beacons.append((x, y))
    
    vertices = []
    for i in range(n):
        j = (i + 1) % n
        dx, dy = beacons[j][0] - beacons[i][0], beacons[j][1] - beacons[i][1]
        vertices.append((beacons[i][0], beacons[i][1]))
    
    total_area = area_polygon(vertices)
    print("{:.1f}".format(total_area))