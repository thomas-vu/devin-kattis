import math

def min_cost_box(V):
    # Start with the smallest possible box dimensions, which is a cube
    min_cost = float('inf')
    for l in range(1, int(V**0.5) + 1):
        if V % l == 0:
            w = V // l
            h = l
            surface_area = 2 * (l*w + w*h + h*l)
            min_cost = min(min_cost, surface_area)
    return min_cost

# Read input from stdin
V = int(input().strip())
print(min_cost_box(V))