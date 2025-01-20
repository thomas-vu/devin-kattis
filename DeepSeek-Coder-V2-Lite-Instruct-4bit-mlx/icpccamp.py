def find_smallest_d(n, p, q, s, classical, creative):
    # Sort the difficulties of both types of problems
    classical.sort()
    creative.sort()
    
    # Initialize the smallest difference to a large number
    min_diff = float('inf')
    
    # Use two pointers to find the smallest difference
    i, j = 0, 0
    while i < p and j < q:
        # Calculate the sum of difficulties on the current day
        total_difficulty = classical[i] + creative[j]
        
        # Check if the sum exceeds the maximum allowed
        if total_difficulty <= s:
            # Update the smallest difference
            min_diff = min(min_diff, abs(classical[i] - creative[j]))
            
            # Move to the next problem in the classical list
            i += 1
        else:
            # Move to the next problem in the creative list
            j += 1
    
    return min_diff if min_diff != float('inf') else -1

# Read input
n, p, q, s = map(int, input().split())
classical = [int(input()) for _ in range(p)]
creative = [int(input()) for _ in range(q)]

# Output the result
print(find_smallest_d(n, p, q, s, classical, creative))