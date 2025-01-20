def compute_constants(n, coefficients):
    constants = [0] * (n + 1)
    constants[0] = coefficients[0]
    
    for i in range(1, n + 1):
        constants[i] = coefficients[i] / i
    
    for i in range(1, n + 1):
        constants[i] = constants[i - 1] + constants[i]
    
    return [int(c) for c in constants]

# Read input from stdin
import sys
input_line = sys.stdin.readline().strip()
n, *coefficients = map(int, input_line.split())

# Compute and print the constants
constants = compute_constants(n, coefficients)
print(' '.join(map(str, constants)))