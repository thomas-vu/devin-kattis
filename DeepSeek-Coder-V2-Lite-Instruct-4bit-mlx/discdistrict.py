import math
r = int(input())
min_dist = float('inf')
best_point = (0, 0)
for x in range(-r-1, r+2):
    for y in range(-r-1, r+2):
        if x*x + y*y > r*r and math.gcd(abs(x), abs(y)) == 1:
            dist = math.sqrt(x*x + y*y)
            if dist < min_dist:
                min_dist = dist
                best_point = (x, y)
print(best_point[0], best_point[1])