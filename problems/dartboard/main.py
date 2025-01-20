import math

def expected_score(radii, sigma):
    # Define the areas of each region on the dartboard
    area_bullseye = math.pi * radii[0]**2
    area_bulls_eye = math.pi * (radii[1]**2 - radii[0]**2)
    areas_pies = [math.pi * (radii[i+2]**2 - radii[i+1]**2) for i in range(4)]
    areas_triple = [area_bulls_eye] + [3 * area for area in areas_pies[:-1]]
    areas_double = [2 * area for area in areas_pies] + [area_bulls_eye]
    
    # Define the probabilities of hitting each region based on the Gaussian distribution
    def prob_region(r, area):
        if r < 1e-9:  # If the dart is at the center, it hits the bullseye
            return area / area_bullseye * 50
        density = (1 / (2 * math.pi * sigma**2)) * math.exp(-(r**2) / (2 * sigma**2))
        return density * area
    
    # Calculate the expected score by integrating over each region
    total_area = math.pi * radii[-1]**2
    expected_score = 0
    for r in [radii[0], radii[1], radii[2], radii[3], radii[4]]:
        if r <= radii[0]:  # Bullseye region
            expected_score += prob_region(r, area_bullseye) * 50
        elif r <= radii[1]:  # Bulls-eye annulus region
            expected_score += prob_region(r, area_bulls_eye) * 25
        elif r <= radii[2]:  # Inner triple ring region
            expected_score += prob_region(r, area_bulls_eye) * 25
        elif r <= radii[3]:  # Inner double ring region
            expected_score += prob_region(r, areas_pies[0]) * 1
        elif r <= radii[4]:  # Outer double ring region
            expected_score += prob_region(r, areas_pies[1]) * 2
        elif r <= radii[5]:  # Outer triple ring region
            expected_score += prob_region(r, areas_pies[2]) * 3
        else:  # Outside the double ring region
            expected_score += prob_region(r, areas_pies[3]) * 4
    
    return expected_score / total_area

# Read input
radii = list(map(float, input().split()))
sigma = float(input())

# Calculate and print the expected score
print("{:.10f}".format(expected_score(radii, sigma)))