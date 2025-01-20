a, b, c, d = map(int, input().split())
p = a**2 + b**2
q = c**2 + d**2

# Find two ways to write p*q as a sum of two squares
x1 = a * c - b * d
y1 = a * d + b * c
x2 = a * c + b * d
y2 = b * c - a * d

# Check if the solutions are valid (integers)
if x1 % 1 == 0 and y1 % 1 == 0:
    print(f"{int(x1)}^2 + {int(y1)}^2 = {p*q}")
if x2 % 1 == 0 and y2 % 1 == 0:
    print(f"{int(x2)}^2 + {int(y2)}^2 = {p*q}")