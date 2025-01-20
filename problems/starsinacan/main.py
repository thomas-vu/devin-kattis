import math

def min_cylinder_volume(stars):
    n = len(stars)
    if n < 4:
        return 0.0
    
    min_volume = float('inf')
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                p1 = stars[i]
                p2 = stars[j]
                p3 = stars[k]
                
                v1 = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
                v2 = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
                
                cross_product = [v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0]]
                len_cross = math.sqrt(sum([x**2 for x in cross_product]))
                
                if len_cross == 0:
                    continue
                
                for l in range(n):
                    if l != i and l != j and l != k:
                        p4 = stars[l]
                        projection_length = ((p4[0] - p1[0])*cross_product[0] + (p4[1] - p1[1])*cross_product[1] + (p4[2] - p1[2])*cross_product[2]) / len_cross
                        if projection_length**2 > min_volume:
                            break
                
                volume = math.pi * (projection_length**2) * sum([x**2 for x in v1])
                min_volume = min(min_volume, volume)
    
    return math.sqrt(min_volume)

# Read input and process the stars
n = int(input().strip())
stars = [list(map(int, input().strip().split())) for _ in range(n)]

# Calculate and output the minimum volume of the cylinder
print("{:.8f}".format(min_cylinder_volume(stars)))