import numpy as np

# Read input points
points = [list(map(int, input().split())) for _ in range(4)]

# Construct the matrix A and vector B for the system of equations
A = np.array([[2*x, 2*y, 2*z] for x, y, z in points])
B = np.array([x**2 + y**2 + z**2 for x, y, z in points])

# Solve the system of equations to find the center of the sphere
center = np.linalg.lstsq(A, B, rcond=None)[0]

# Output the center coordinates rounded to 7 decimal places
print("{:.7f} {:.7f} {:.7f}".format(*center))