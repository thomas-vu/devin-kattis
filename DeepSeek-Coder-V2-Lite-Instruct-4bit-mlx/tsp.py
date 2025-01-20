import sys
import math
from itertools import permutations

def dist(point1, point2):
    return round(math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

def tsp(points):
    n = len(points)
    dist_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist_matrix[i][j] = dist_matrix[j][i] = dist(points[i], points[j])
    
    min_tour_cost = float('inf')
    best_tour = None
    
    for perm in permutations(range(n)):
        tour_cost = 0
        for i in range(n - 1):
            tour_cost += dist_matrix[perm[i]][perm[i + 1]]
        tour_cost += dist_matrix[perm[-1]][perm[0]]
        
        if tour_cost < min_tour_cost:
            min_tour_cost = tour_cost
            best_tour = perm
    
    return [point + 1 for point in best_tour]

# Read input
n = int(sys.stdin.readline().strip())
points = [tuple(map(float, sys.stdin.readline().split())) for _ in range(n)]

# Solve TSP
tour = tsp(points)

# Output the tour
for point_index in tour:
    print(point_index)