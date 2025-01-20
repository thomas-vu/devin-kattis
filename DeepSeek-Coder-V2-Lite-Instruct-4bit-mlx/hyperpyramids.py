# Python code to solve the problem of computing Pascal's hyper-pyramid base for a given dimension D and height H.

def generate_base(D, H):
    # Initialize the base of Pascal's hyper-pyramid with 1's
    base = [[[1 for _ in range(H+1)] for _ in range(D+1)]
    
    # Fill the base using Pascal's rule for hyper-pyramid
    for z in range(1, H+1):
        for y in range(1, D+1):
            for x in range(1, z+y-D+2):
                base[x][y][z] = base[x-1][y][z] + base[x][y-1][z] + base[x][y][z-1]
    
    # Extract the unique values at the base of the hyper-pyramid
    base_values = set()
    for y in range(H+1):
        for x in range(y, D+x-H+2):
            base_values.add(base[x][y][H])
    
    # Return the sorted set of base values
    return sorted(base_values)

# Read input from stdin
D, H = map(int, input().split())

# Generate and print the base of Pascal's hyper-pyramid
base_values = generate_base(D, H)
for value in base_values:
    print(value)