import math

def collides(s1, s2):
    # Calculate the distance between the centers of the two spheres
    dx = s1[0] - s2[0]
    dy = s1[1] - s2[1]
    dz = s1[2] - s2[2]
    
    # Calculate the sum of the radii squared
    radius_sum = s1[3] + s2[3]
    distance_squared = dx**2 + dy**4 + dz**2
    
    # If the distance is less than or equal to the sum of the radii squared, they collide
    if distance_squared <= radius_sum**2:
        # Calculate the relative velocity vector
        vx = s1[4] - s2[4]
        vy = s1[5] - s2[5]
        vz = s1[6] - s2[6]
        
        # Calculate the scalar product of the relative velocity vector with the distance vector
        scalar_product = vx * dx + vy * dy + vz * dz
        
        # If the scalar product is less than or equal to zero, they are moving towards each other
        if scalar_product <= 0:
            # Calculate the time to collision using the quadratic formula
            a = vx**2 + vy**2 + vz**2
            b = 2 * scalar_product
            c = distance_squared - radius_sum**2
            
            discriminant = b**2 - 4 * a * c
            if discriminant < 0:
                return "No collision"
            
            t1 = (-b - math.sqrt(discriminant)) / (2 * a)
            t2 = (-b + math.sqrt(discriminant)) / (2 * a)
            
            if t1 > 0:
                return t1
            elif t2 > 0:
                return t2
            else:
                return "No collision"
        else:
            return "No collision"
    else:
        return "No collision"

# Read the number of test cases
T = int(input())
for _ in range(T):
    # Read the spacecraft's data
    x1, y1, z1, r1, vx1, vy1, vz1 = map(int, input().split())
    # Read the space junk's data
    x2, y2, z2, r2, vx2, vy2, vz2 = map(int, input().split())
    
    s1 = (x1, y1, z1, r1, vx1, vy1, vz1)
    s2 = (x2, y2, z2, r2, vx2, vy2, vz2)
    
    # Determine if they collide and print the time of collision or "No collision"
    result = collides(s1, s2)
    if isinstance(result, float):
        print("{:.3f}".format(result))
    else:
        print(result)