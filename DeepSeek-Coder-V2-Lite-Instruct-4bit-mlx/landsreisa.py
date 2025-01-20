import sys
from itertools import permutations
import math

def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

def calculate_score(route, locations):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += euclidean_distance(locations[route[i]], locations[route[i+1]])
    return total_distance

def main():
    n = int(input())
    locations = []
    for _ in range(n):
        x, y = map(float, input().split())
        locations.append((x, y))
    
    min_distance = float('inf')
    best_route = None
    
    for route in permutations(range(1, n)):
        current_distance = 0
        for i in range(n - 1):
            current_distance += euclidean_distance(locations[0], locations[route[i]])
        if current_distance < min_distance:
            min_distance = current_distance
            best_route = [0] + list(route)
    
    print(' '.join(map(str, best_route)))

if __name__ == "__main__":
    main()