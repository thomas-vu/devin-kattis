def calculate_area(d, a, b, h):
    # Calculate the area of Mahjong's pizza
    mahjong_area = (d / 2) ** 2 * 3.141592653589793
    
    # Calculate the area of Trapizza's pizza
    trapizza_area = 0.5 * (a + b) * h
    
    return mahjong_area, trapizza_area

# Read inputs
d = int(input())
a = int(input())
b = int(input())
h = int(input())

# Calculate areas
mahjong_area, trapizza_area = calculate_area(d, a, b, h)

# Compare areas and output the result
if mahjong_area > trapizza_area:
    print("Mahjong!")
elif trapizza_area > mahjong_area:
    print("Trapizza!")
else:
    print("Jafn storar!")