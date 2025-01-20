def optimal_water_height(h, r, da, dw):
    from math import pi
    
    # Calculate the volume of the bottle
    V_bottle = pi * r**2 * h
    
    # Define the function for centre of mass
    def centre_of_mass(water_height):
        # Volume of water in the bottle
        V_water = pi * r**2 * water_height
        
        # Mass of air and mass of water
        m_air = V_bottle * da
        m_water = V_water * dw
        
        # Centre of mass of air and water
        cm_air = V_bottle / 2
        cm_water = (V_bottle + V_water) / 2 - m_air * (h - water_height) / m_water
        
        return cm_water
    
    # Binary search for the optimal water height
    left, right = 0, h
    while right - left > 1e-6:
        mid = (left + right) / 2
        if centre_of_mass(mid) < h / 2:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2

# Read input
import sys
input_data = sys.stdin.read().splitlines()
h, r, da, dw = map(int, input_data[0].split())

# Calculate and output the result
result = optimal_water_height(h, r, da, dw)
print("{:.10f}".format(result))