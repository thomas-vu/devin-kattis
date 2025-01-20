import math

# Read the coefficients of the polynomial from input
a = int(input())
b = int(input())
c = int(input())

# Calculate the discriminant of the polynomial
discriminant = b**2 - 4*a*c

# Determine the number of real roots based on the discriminant
if discriminant > 0:
    print(2)
elif discriminant == 0:
    print(1)
else:
    print(0)