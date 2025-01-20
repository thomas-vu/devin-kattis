import math

def tangential_coordinates(x, y):
    radius = math.sqrt(x**2 + y**2)
    if radius <= 1:
        return None
    
    distance_from_center = math.sqrt(x**2 + y**2)
    angle = math.atan2(y, x)
    
    a1 = -x / distance_from_center
    b1 = -y / distance_from_center
    c1 = 1
    
    a2 = x / distance_from_center
    b2 = y / distance_from_center
    c2 = 1
    
    return (a1, b1, c1, a2, b2, c2)

def main():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(float, input().split())
        points.append((x, y))
    
    for x, y in points:
        coords = tangential_coordinates(x, y)
        if coords is not None:
            a1, b1, c1, a2, b2, c2 = coords
            print(f"({a1},{b1},{c1},{a2},{b2},{c2})")

if __name__ == "__main__":
    main()