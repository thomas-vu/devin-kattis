def linear_congruential_generator(a, b, x0, n, m):
    if n == 0:
        return x0
    
    # Calculate the sequence using the linear congruential formula
    for _ in range(n):
        x0 = (a * x0 + b) % m
    
    return x0

# Read input from stdin
a, b, x0, n, m = map(int, input().split())

# Output the n-th random number
print(linear_congruential_generator(a, b, x0, n, m))