import itertools
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_collinear(x1, y1, x2, y2, x3, y3):
    return (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0

def largest_triangle(n, lines):
    max_perimeter = 0.0
    
    for (i1, i2, i3) in itertools.combinations(range(n), 3):
        x1, y1, x2, y2 = lines[i1]
        x3, y3, x4, y4 = lines[i2]
        x5, y5, x6, y6 = lines[i3]
        
        if check_collinear(x1, y1, x2, y2, x3, y3) or check_collinear(x1, y1, x2, y2, x4, y4) or check_collinear(x1, y1, x2, y2, x5, y5) or check_collinear(x1, y1, x2, y2, x6, y6) or check_collinear(x3, y3, x4, y4, x5, y5) or check_collinear(x3, y3, x4, y4, x6, y6) or check_collinear(x3, y3, x5, y5, x6, y6) or check_collinear(x4, y4, x5, y5, x6, y6):
            continue
        
        a = distance(x1, y1, x2, y2)
        b = distance(x3, y3, x4, y4)
        c = distance(x5, y5, x6, y6)
        
        if a + b > c and a + c > b and b + c > a:
            perimeter = a + b + c
            max_perimeter = max(max_perimeter, perimeter)
    
    return max_perimeter if max_perimeter > 0.0 else "no triangle"

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
print("{:.10f}".format(largest_triangle(n, lines)))