def find_polynomial_degree_and_next_value(sequence):
    n = len(sequence)
    differences = [sequence[i+1] - sequence[i] for i in range(n-1)]
    
    degree = 0
    while all(diff == differences[0] for diff in differences):
        degree += 1
        if degree >= n:
            break
        differences = [differences[i+1] - differences[i] for i in range(len(differences)-1)]
    
    constant_diff = differences[0] if len(differences) > 0 else 0
    next_value = sequence[-1] + constant_diff
    
    return degree, next_value

# Read input
n = int(input())
sequence = list(map(int, input().split()))

# Process the sequence and output the result
degree, next_value = find_polynomial_degree_and_next_value(sequence)
print(degree, next_value)