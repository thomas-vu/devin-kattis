import sys
from itertools import permutations

def distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(stops):
    unique_pokemon = set()
    for stop in stops:
        _, pokemon = stop.split(' ', 1)
        unique_pokemon.add(pokemon)
    
    min_distance = float('inf')
    for perm in permutations(stops):
        current_distance = 0
        prev_stop = (0, 0)
        for stop in perm:
            _, _ = map(int, stop.split(' ', 1)[0].split())
            current_distance += distance(prev_stop, new_stop)
            prev_stop = new_stop
        current_distance += distance(prev_stop, (0, 0))
        min_distance = min(min_distance, current_distance)
    
    return min_distance

# Read input
n = int(sys.stdin.readline().strip())
stops = [sys.stdin.readline().strip() for _ in range(n)]

# Solve the problem
result = solve(stops)

# Output the result
print(result)