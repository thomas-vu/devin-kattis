import sys
from math import sqrt, atan2, pi

def min_distance_to_parakoopas(n, parakoopas):
    # Sort the parakoopas by their x-coordinates
    parakoopas.sort(key=lambda p: p[0])
    
    # Calculate the minimum distance using a brute-force approach for small inputs
    if n <= 2:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                min_dist = min(min_dist, sqrt((parakoopas[i][0] - parakoopas[j][0]) ** 2 + (parakoopas[i][1] - parakoopas[j][1]) ** 2))
        return min_dist
    
    # For larger inputs, use a more sophisticated approach
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    
    def can_hit_two(d):
        # Check if there are at least two parakoopas within the distance d of each other
        for i in range(n):
            for j in range(i + 1, n):
                if distance(parakoopas[i], parakoopas[j]) <= d:
                    return True
        return False
    
    # Binary search for the minimum distance
    left, right = 0.0, min(distance((0, 0), parakoopas[i]) for i in range(n))
    while right - left > 1e-6:
        mid = (left + right) / 2.0
        if can_hit_two(mid):
            right = mid
        else:
            left = mid
    
    return (left + right) / 2.0

# Read input
n = int(input().strip())
parakoopas = [tuple(map(int, input().strip().split())) for _ in range(n)]

# Calculate and output the result
result = min_distance_to_parakoopas(n, parakoopas)
print("{:.6f}".format(result))