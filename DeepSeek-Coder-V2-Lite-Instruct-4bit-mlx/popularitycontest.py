def calculate_marketability_coefficients(N, M, friendships):
    # Initialize popularity and success factors with default values
    popularity = [0] * (N + 1)
    
    # Process friendships to update popularity factors
    for a, b in friendships:
        popularity[a] += 1
        popularity[b] += 1
    
    # Calculate marketability coefficients
    success_factors = [i for i in range(1, N + 1)]
    marketability_coefficients = [popularity[i] - success_factors[i - 1] for i in range(N)]
    
    return marketability_coefficients[1:]  # Exclude the first element which is unused

# Read input
N, M = map(int, input().split())
friendships = [tuple(map(int, input().split())) for _ in range(M)]

# Calculate and print the marketability coefficients
coefficients = calculate_marketability_coefficients(N, M, friendships)
print(' '.join(map(str, coefficients)))