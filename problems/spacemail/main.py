import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def max_distance(planets):
    n = len(planets)
    if n == 2:
        return int(distance(planets[0], planets[1])) + 1
    
    max_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(planets[i], planets[j])
            max_dist = max(max_dist, dist)
    
    return int(math.ceil(max_dist))

n = int(input())
planets = [tuple(map(int, input().split())) for _ in range(n)]
print(max_distance(planets))