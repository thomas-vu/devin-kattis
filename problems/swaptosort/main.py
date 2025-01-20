def can_sort_array(N, K, swaps):
    # Create a list to track the position of each element in the original array
    positions = [i for i in range(N + 1)]
    
    # Apply the swaps to the positions list
    for a, b in swaps:
        positions[a], positions[b] = positions[b], positions[a]
    
    # Check if the array can be sorted by verifying the positions list
    for i in range(1, N + 1):
        if positions[i] != i:
            return "No"
    return "Yes"

# Read input from stdin
N, K = map(int, input().split())
swaps = [tuple(map(int, input().split())) for _ in range(K)]

# Output the result
print(can_sort_array(N, K, swaps))