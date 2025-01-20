def calculate_passes(K, desk_numbers):
    passes = 0
    current_position = 1
    
    for desk in desk_numbers:
        if desk < current_position:
            passes += 1
            current_position = 1
        while desk != current_position:
            passes += 1
            current_position += 1
    
    return passes + K - 1

# Read input
K = int(input())
desk_numbers = [int(input()) for _ in range(K)]

# Calculate and print the result
print(calculate_passes(K, desk_numbers))