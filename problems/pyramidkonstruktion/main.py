def min_extra_bricks(H, N, M):
    # Calculate the number of bricks needed for a complete pyramid of height H
    total_bricks = 0
    for k in range(1, H + 1):
        total_bricks += (2 * k) ** 2
    
    # Calculate the number of bricks Kim already has
    existing_bricks = N * 4 + M * 16
    
    # Calculate the number of extra bricks needed
    extra_2x2 = max(0, (total_bricks - existing_bricks) // 4)
    extra_4x2 = max(0, (total_bricks - existing_bricks) % 4 // 1)
    
    return extra_2x2, extra_4x2

# Read input
H, N, M = map(int, input().split())

# Get the result
A, B = min_extra_bricks(H, N, M)

# Output the result
print(A, B)