import math

def euclidean_area(R):
    return math.pi * R**2

def taxicab_area(R):
    return 2 * (R**2)

# Read the radius from input
R = float(input())

# Calculate and print the areas
euclidean_area_result = euclidean_area(R)
taxicab_area_result = taxicab_area(R)

print("{:.6f}".format(euclidean_area_result))
print("{:.6f}".format(taxicab_area_result))