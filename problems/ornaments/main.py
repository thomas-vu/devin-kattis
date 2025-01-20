import math

def calculate_string_length(r, h, s):
    # Calculate the circumference of the circle
    circumference = 2 * math.pi * r
    
    # Calculate the straight distance from the knot to the center of the circle
    straight_distance = math.sqrt(h**2 - r**2)
    
    # Calculate the total length of the string without the excess
    total_length = circumference + straight_distance * 2
    
    # Apply the excess string multiplier
    total_length *= (1 + s / 100)
    
    # Return the total length rounded to two decimals
    return round(total_length, 2)

# Read input until three zeros are encountered
while True:
    r, h, s = map(int, input().split())
    if r == 0 and h == 0 and s == 0:
        break
    print(f"{calculate_string_length(r, h, s):.2f}")