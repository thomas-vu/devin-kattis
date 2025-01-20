import math

def hit_time(n, omega, v0, theta, w):
    # Convert initial angle to radians
    theta_rad = math.radians(theta)
    
    # Calculate the velocity components
    v0x = v0 * math.cos(theta_rad)
    v0y = v0 * math.sin(theta_rad)
    
    # Calculate the time to hit the wall for each corner
    times = []
    for _ in range(n):
        x0, y0 = map(float, input().split())
        # Calculate the time to hit the wall for this corner
        a = 0.5 * (-9.81) / (v0x ** 2)
        b = y0 - v0y / v0x * x0 + omega * x0
        c = (-w - x0)
        
        # Discriminant of the quadratic equation
        discriminant = b**2 - 4*a*c
        
        # Check if the cookie hits the wall
        if discriminant >= 0:
            t1 = (-b + math.sqrt(discriminant)) / (2*a)
            t2 = (-b - math.sqrt(discriminant)) / (2*a)
            
            # Use the smaller positive time value
            if t1 > 0:
                times.append((t1, _ + 1))
            elif t2 > 0:
                times.append((t2, _ + 1))
    
    # Return the corner with the smallest time to hit the wall
    if times:
        min_time = min(times, key=lambda x: x[0])
        return min_time
    else:
        return None

# Read input
n, omega, v0, theta, w = map(float, input().split())
theta = int(theta)
# Read the vertices of the cookie polygon
vertices = [tuple(map(float, input().split())) for _ in range(int(n))]

# Find the corner that hits the wall first
result = hit_time(int(n), omega, v0, theta, w)
if result:
    print("{:.3f}".format(result[0]), int(result[1]))