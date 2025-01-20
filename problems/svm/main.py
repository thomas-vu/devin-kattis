import sys
import numpy as np

# Read the number of dimensions and SVM parameters
n = int(input())
w_b = list(map(float, input().split()))
w = np.array(w_b[:-1])
b = w_b[-1]

# Function to calculate the distance from a point x to the hyperplane
def distance_to_hyperplane(x, w, b):
    return (np.dot(w, x) + b) / np.linalg.norm(w)

# Read and process each query point
for line in sys.stdin:
    x = np.array(list(map(float, line.split())))
    d = distance_to_hyperplane(x, w, b)
    print("{:.4f}".format(d))