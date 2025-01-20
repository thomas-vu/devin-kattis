def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def convert_temperature(unit_systems, x, y, v):
    # Extract the coefficients for the linear transformation from Celsius to the unit system x and y
    a_x, b_x = unit_systems[x - 1]
    a_y, b_y = unit_systems[y - 1]
    
    # Calculate the transformation coefficients from Celsius to unit system x and y
    c_x = (b_x - a_x) / 100.0
    c_y = (b_y - a_y) / 100.0
    
    # Convert the temperature v from unit system x to Celsius, then to unit system y
    celsius_v = (v - a_x) / c_x
    y_v = a_y + c_y * celsius_v
    
    # Reduce the fraction to its simplest form
    g = gcd(int(y_v), 100)
    if y_v < 0:
        return f"{-int(-y_v // g)}/{100 // g}"
    else:
        return f"{int(y_v // g)}/{100 // g}"

# Read input
N, Q = map(int, input().split())
unit_systems = []
for _ in range(N):
    a, b = map(int, input().split())
    unit_systems.append((a, b))

# Process queries
for _ in range(Q):
    x, y, v = map(int, input().split())
    print(convert_temperature(unit_systems, x, y, v))