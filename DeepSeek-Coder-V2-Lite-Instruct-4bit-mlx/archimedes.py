import math

def archimedes_spiral(b, tx, ty):
    # Calculate the angle needed to reach the target in one full rotation
    radius_at_one_rotation = 2 * math.pi * b
    
    # Calculate the angle needed to reach the target in half a rotation
    radius_at_half_rotation = math.pi * b
    
    # Calculate the angle needed to reach the target in one quarter of a rotation
    radius_at_quarter_rotation = 0.5 * math.pi * b
    
    # Initialize the angle
    phi = 0
    
    while True:
        r = b * phi
        
        # Calculate the distance from the spiral point to the target
        distance_to_target = math.sqrt((r * math.cos(phi) - tx)**2 + (r * math.sin(phi) - ty)**2)
        
        # Check if the target is reached within one full rotation
        if distance_to_target <= 10**-3:
            return (r * math.cos(phi), r * math.sin(phi))
        
        # Check if the target is reached within half a rotation
        elif radius_at_half_rotation - distance_to_target < 10**-3:
            return (r * math.cos(phi), r * math.sin(phi))
        
        # Check if the target is reached within one quarter of a rotation
        elif radius_at_quarter_rotation - distance_to_target < 10**-3:
            return (r * math.cos(phi), r * math.sin(phi))
        
        # Increment the angle for the next point on the spiral
        phi += 0.01

# Example usage:
b, tx, ty = 0.5, -5.301, 3.098
print(archimedes_spiral(b, tx, ty))