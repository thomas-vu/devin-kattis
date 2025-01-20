import math
from itertools import permutations

def time_to_reach(cat_pos, mouse_pos, initial_velocity):
    distance = math.sqrt((mouse_pos[0] - cat_pos[0])**2 + (mouse_pos[1] - cat_pos[1])**2)
    return distance / initial_velocity

def solve(n, mice, m):
    min_initial_velocity = float('inf')
    
    for perm in permutations(mice):
        current_velocity = 1.0
        for i in range(n):
            time_to_reach_mouse = time_to_reach((0, 0), perm[i][:2], current_velocity)
            if time_to_reach_mouse > perm[i][2]:
                break
            current_velocity *= m
        else:
            min_initial_velocity = min(min_initial_velocity, current_velocity)
    
    return min_initial_velocity

# Read input
n = int(input())
mice = [tuple(map(int, input().split())) for _ in range(n)]
m = float(input())

# Solve the problem and output the result
result = solve(n, mice, m)
print("{:.10f}".format(result))