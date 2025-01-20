import numpy as np
from scipy.optimize import minimize

def euclidean_distance(vec1, vec2):
    return np.linalg.norm(np.array(vec1) - np.array(vec2))

def objective_function(unknown_vector, known_vectors, distances):
    total_error = 0.0
    for vec, dist in zip(known_vectors, distances):
        total_error += (euclidean_distance(vec, unknown_vector) - dist) ** 2
    return total_error

def find_unknown_vector(known_vectors, distances):
    initial_guess = [0.0] * len(known_vectors[0])
    result = minimize(objective_function, initial_guess, args=(known_vectors, distances), method='L-BFGS-B')
    return result.x

# Read input
d, n = map(int, input().split())
known_vectors = []
distances = []
for _ in range(n):
    vec = list(map(float, input().split()[:-1]))
    dist = float(input().split()[-1])
    known_vectors.append(vec)
    distances.append(dist)

# Find the unknown vector
unknown_vector = find_unknown_vector(known_vectors, distances)

# Output the result
for coord in unknown_vector:
    print("{:.17f}".format(coord), end=' ')