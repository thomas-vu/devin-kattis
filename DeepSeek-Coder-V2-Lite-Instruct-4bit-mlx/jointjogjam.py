import math

def max_distance(kx, ky, ox, oy, ex, ey):
    # Calculate the distance between Kari's starting and ending points
    dk = math.sqrt((ex - kx)**2 + (ey - ky)**2)
    # Calculate the distance between Ola's starting and ending points
    do = math.sqrt((ex - ox)**2 + (ey - oy)**2)
    # Calculate the distance between Kari's starting and Ola's ending points
    dko = math.sqrt((ox - kx)**2 + (oy - ky)**2)
    # Calculate the distance between Ola's starting and Kari's ending points
    dkoo = math.sqrt((kx - ox)**2 + (ky - oy)**2)
    
    # Use the properties of triangles to find the maximum distance between Kari and Ola during the run
    # The maximum distance will be the farthest point of either Kari or Ola's path
    max_dist = max(dk, do, dko, dkoo)
    
    return max_dist

# Read input
kx, ky = map(int, input().split())
ox, oy = map(int, input().split())
ex, ey = map(int, input().split())

# Calculate and output the result
result = max_distance(kx, ky, ox, oy, ex, ey)
print("{:.10f}".format(result))