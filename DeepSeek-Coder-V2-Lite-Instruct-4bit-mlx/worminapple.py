import sys
from itertools import combinations
from math import sqrt, isclose

def distance(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)

def sign(p1, p2, p3):
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

def point_inside_triangle(pt, v1, v2, v3):
    d1 = sign(pt, v1, v2)
    d2 = sign(pt, v2, v3)
    d3 = sign(pt, v3, v1)

    has_neg = (d1 < 0.0) or (d2 < 0.0) or (d3 < 0.0)
    has_pos = (d1 > 0.0) or (d2 > 0.0) or (d3 > 0.0)

    return not (has_neg and has_pos)

def point_inside_convex(pt, vertices):
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        if sign(pt, vertices[i], vertices[j]) < 0.0:
            return False
    return True

def minimum_distance_to_surface(pt, vertices):
    min_dist = float('inf')
    for i in range(len(vertices)):
        j = (i + 1) % len(vertices)
        edge_vector = tuple((vertices[j][k] - vertices[i][k]) for k in range(3))
        point_on_edge = tuple((vertices[i][k] + edge_vector[k]) for k in range(3))
        dist = distance(pt, point_on_edge)
        min_dist = min(min_dist, dist)
    return min_dist

# Read input
n = int(input())
vertices = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
q = int(input())
queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(q)]

# Calculate minimum distance for each query point
for query in queries:
    min_dist = minimum_distance_to_surface(query, vertices)
    print("{:.10f}".format(min_dist))