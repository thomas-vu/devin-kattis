import sys
from itertools import permutations

# Function to extract the plaintext and ciphertext from the input lines
def extract_data(lines):
    n = int(lines[0].strip())
    plaintext = lines[1].replace(" ", "").upper()
    ciphertext = lines[2].replace(" ", "").upper()
    return n, plaintext, ciphertext

# Function to generate the matrix from a given permutation of key elements
def generate_matrix(permutation, plaintext, ciphertext):
    n = len(permutation)
    matrix = [[0] * n for _ in range(n)]
    for i in range(len(plaintext) // n):
        for j in range(n):
            matrix[j][i % n] = ord(ciphertext[i * n + j]) - ord(plaintext[i * n + j])
    return matrix

# Function to check if the generated matrix is valid for all plaintext/ciphertext pairs
def is_valid(matrix, plaintext, ciphertext):
    for i in range(len(plaintext) // len(matrix)):
        encrypted = [0] * len(matrix)
        for j in range(len(matrix)):
            for k in range(len(matrix[0])):
                encrypted[j] += matrix[j][k] * ord(plaintext[(i * len(matrix)) + k])
        for j in range(len(encrypted)):
            if encrypted[j] % 26 != ord(ciphertext[(i * len(matrix)) + j]) - ord('A'):
                return False
    return True

# Main function to solve the problem
def main():
    lines = sys.stdin.readlines()
    n, plaintext, ciphertext = extract_data(lines)
    
    # Generate all possible permutations of the key elements
    key_elements = list(range(26))
    solutions = []
    
    for perm in permutations(key_elements):
        matrix = generate_matrix(perm, plaintext, ciphertext)
        if is_valid(matrix, plaintext, ciphertext):
            solutions.append(perm)
    
    if len(solutions) == 0:
        print("No solution")
    elif len(solutions) > 1:
        print("Too many solutions")
    else:
        for element in solutions[0]:
            print(chr(element + ord('A')), end=' ')
        print()

if __name__ == "__main__":
    main()