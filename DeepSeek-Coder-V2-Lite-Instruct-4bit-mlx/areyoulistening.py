import math
from itertools import combinations

def distance(cx, cy, x, y):
    return math.sqrt((cx - x)**2 + (cy - y)**2)

def can_detect(cx, cy, radius, x, y, r):
    dist = distance(cx, cy, x, y)
    return dist <= radius + r

def main():
    cx, cy, n = map(int, input().split())
    devices = [tuple(map(int, input().split())) for _ in range(n)]
    
    max_radius = 0
    for a, b in combinations(devices, 2):
        x1, y1, r1 = a
        x2, y2, r2 = b
        
        if can_detect(x1, y1, 0, x2, y2, r2) or can_detect(x2, y2, 0, x1, y1, r1):
            continue
        
        d = distance(x1, y1, x2, y2)
        if d + r1 <= max(r2, max_radius):
            continue
        
        if d + r2 <= max(r1, max_radius):
            continue
        
        min_r = (d + r1 + r2) / 2
        if min_r > max_radius:
            max_radius = int(min_r) - 1
    
    print(max_radius)

main()