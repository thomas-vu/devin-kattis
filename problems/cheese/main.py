import sys
from math import pi

def volume_hole(r):
    return (4/3) * pi * r**3

def main():
    n, s = map(int, sys.stdin.readline().split())
    holes = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    # Calculate the total volume of cheese excluding holes
    total_cheese = 100**3
    for r, x, y, z in holes:
        total_cheese -= volume_hole(r)
    
    # Calculate the desired slice thickness
    slice_thickness = total_cheese / s
    
    # Calculate the minimum thickness for each slice considering holes
    min_thicknesses = []
    for r, x, y, z in holes:
        hole_volume = volume_hole(r)
        for slice_z in range(int(z), int(z)+100, 1):
            if (x-r)**2 + (y-r)**2 > r**2:
                continue  # Hole is outside the current slice
            if (x+r)**2 + (y+r)**2 <= r**2:
                continue  # Hole is outside the current slice
            min_thicknesses.append((z, hole_volume))
            break
    
    # Sort min_thicknesses by z coordinate (bottom to top)
    min_thicknesses.sort(key=lambda x: x[0])
    
    # Calculate the thickness of each slice from top to bottom
    slice_thicknesses = []
    for i in range(s):
        if i == 0:
            slice_thicknesses.append((min_thicknesses[-1-i][1] / 100**2) ** (1/3))
        else:
            slice_thicknesses.append((min_thicknesses[-1-i][1] / 100**2) ** (1/3))
    
    # Output the slice thicknesses
    for t in reversed(slice_thicknesses):
        print("{:.10f}".format(t))

if __name__ == "__main__":
    main()