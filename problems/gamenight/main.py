def min_swaps(s, n):
    # Count the number of swaps needed for each team configuration
    min_swaps = float('inf')
    
    # Check for each possible team configuration (ABC, ACB, BAC, etc.)
    for target in 'ABC':
        swaps = 0
        # Compare the current configuration with the target configuration
        for i in range(n):
            if s[i] != target:
                swaps += 1
        # Update the minimum swaps for this configuration
        min_swaps = min(min_swaps, swaps)
    
    return min_swaps

# Read input from stdin
n = int(input())
s = input()

# Calculate and print the minimum number of swaps needed
print(min_swaps(s, n))