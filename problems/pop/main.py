import sys
import math

def sign(x):
    return (1 if x > 0 else (-1 if x < 0 else 0))

def intersect_balloons(p, v, balloon):
    r = balloon[0]
    s = balloon[1]
    x, y = balloon[2], balloon[3]
    
    a = v[0]**2 + v[1]**2 + v[2]**2
    b = 2 * (v[0]*(p[0]-x) + v[1]*(p[1]-y) + v[2]*(p[2]-s))
    c = (p[0]-x)**2 + (p[1]-y)**2 + (p[2]-s)**2 - r**2
    
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return False
    
    t1 = (-b - math.sqrt(discriminant)) / (2*a)
    t2 = (-b + math.sqrt(discriminant)) / (2*a)
    
    if t1 > 0 and t2 > 0:
        return True
    
    return False

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        balloons = [list(map(float, input().split())) for _ in range(n)]
        m = int(input())
        
        for _ in range(m):
            p = list(map(float, input().split()))
            v = list(map(float, input().split()))
            
            points = 0
            for balloon in balloons:
                if intersect_balloons(p, v, balloon):
                    points += 1
            
            print(points)

if __name__ == "__main__":
    main()