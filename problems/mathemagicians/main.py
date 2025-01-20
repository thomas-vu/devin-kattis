def can_achieve_desired_configuration(n, initial_hats, desired_hats):
    # Helper function to check if we can achieve the desired configuration starting from a given index
    def is_possible(start):
        hats = list(initial_hats)
        for i in range(start, start + n):
            idx = i % n
            if hats[idx] != desired_hats[idx]:
                # Change the hat color to match the left or right neighbor
                if idx > 0:
                    hats[idx - 1] = 'B' if hats[idx - 1] == 'R' else 'R'
                elif idx < n - 1:
                    hats[idx + 1] = 'B' if hats[idx + 1] == 'R' else 'R'
                else:
                    # Special case for the last mathemagician (wrap around)
                    hats[0] = 'B' if hats[0] == 'R' else 'R'
        # Check if the final configuration matches the desired one
        return all(hats[i] == desired_hats[i] for i in range(n))
    
    # Try to start from each mathemagician's position and check if it's possible
    for i in range(n):
        if is_possible(i):
            return "yes"
    return "no"

# Read input
n = int(input().strip())
initial_hats = input().strip()
desired_hats = input().strip()

# Output the result
print(can_achieve_desired_configuration(n, initial_hats, desired_hats))