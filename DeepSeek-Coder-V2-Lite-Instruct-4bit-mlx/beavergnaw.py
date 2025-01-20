import math

def calculate_inner_diameter(D, V):
    # Calculate the volume of the original cylinder
    original_volume = math.pi * (D / 2)**2 * D
    
    # Calculate the height of the chomped out segment
    chomped_height = D - math.sqrt((D / 2)**2 * (math.pi / 4))
    
    # Calculate the volume of the chomped out segment (two frustums + cylinder)
    if D <= 1:
        chomped_volume = V
    else:
        frustum_height = D - (D / 2) * math.sqrt(1 - (math.pi / 4))
        frustum_volume = (1/3) * math.pi * ((D / 2)**2 + D**2 + (D / 2) * D * math.sqrt(1 - (math.pi / 4)))
        cylinder_volume = math.pi * ((D / 2)**2 - (d / 2)**2) * D
        chomped_volume = 2 * frustum_volume + cylinder_volume
    
    # Set up the equation to solve for d
    def volume_equation(d):
        return math.pi * (D / 2)**2 * D - V - math.pi * (d / 2)**2 * D
    
    # Use a numerical method to solve for d
    def find_d(V):
        low, high = 0, D
        while high - low > 1e-6:
            mid = (low + high) / 2
            if volume_equation(mid) < 0:
                low = mid
            else:
                high = mid
        return (low + high) / 2
    
    d = find_d(V)
    return d

# Read input until EOF
while True:
    D, V = map(int, input().split())
    if D == 0 and V == 0:
        break
    d = calculate_inner_diameter(D, V)
    print("{:.8f}".format(d))