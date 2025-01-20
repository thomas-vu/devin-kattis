import math

def calculate_area(r, x, y):
    # Check if the strike is inside the cookie
    distance = math.sqrt(x**2 + y**2)
    if distance > r:
        return "miss"
    
    # Calculate the angle subtended by the chord at the center of the circle
    theta = 2 * math.asin(distance / (2 * r))
    
    # Calculate the areas of the two resulting pieces
    sector_area = (theta / (2 * math.pi)) * math.pi * r**2
    chord_area = r**2 * (math.sin(theta) / 2)
    piece_area = max(sector_area, r**2 - sector_area + chord_area)
    
    return f"{piece_area:.6f} {r**2 - piece_area:.6f}"

while True:
    try:
        r, x, y = map(float, input().split())
        result = calculate_area(r, x, y)
        print(result)
    except EOFError:
        break