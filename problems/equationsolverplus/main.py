import sys
from fractions import Fraction

def gaussian_elimination(matrix, vector):
    n = len(matrix)
    for i in range(n):
        # Find the pivot row
        pivot_row = i + max(range(i, n), key=lambda x: abs(matrix[x][i]))
        if pivot_row != i:
            matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]
            vector[i], vector[pivot_row] = vector[pivot_row], vector[i]
        
        # Check if the pivot element is zero
        if matrix[i][i] == 0:
            continue
        
        # Make the pivot element 1
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]
            vector[j] -= factor * vector[i]
    
    # Back substitution
    solution = [0] * n
    for i in range(n - 1, -1, -1):
        if matrix[i][i] == 0:
            continue
        solution[i] = vector[i] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            vector[j] -= matrix[j][i] * solution[i]
    
    return solution

def parse_input(input_lines):
    index = 0
    while True:
        n = int(input_lines[index].strip())
        index += 1
        if n == 0:
            break
        
        matrix = []
        for _ in range(n):
            row = list(map(Fraction, input_lines[index].strip().split()))
            index += 1
            matrix.append(row)
        
        vector = list(map(Fraction, input_lines[index].strip().split()))
        index += 1
        
        yield matrix, vector

for matrix, vector in parse_input(sys.stdin):
    solution = gaussian_elimination(matrix, vector)
    
    # Check for consistency
    for row in matrix:
        zero_row = all(x == 0 for x in row)
        if zero_row and not all(x == 0 for x in vector):
            print("inconsistent")
            break
    else:
        for x in solution:
            if isinstance(x, Fraction):
                print("{:.2f}".format(float(x)), end=" ")
            else:
                print("?", end=" ")
        print()