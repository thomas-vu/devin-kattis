def min_initial_tolerance(n, spiciness):
    # Base case: if there's only one slice, no tolerance is needed.
    if n == 1:
        return spiciness[0]
    
    # Sort the spiciness values to facilitate eating in a non-decreasing order.
    sorted_spiciness = sorted(spiciness)
    
    # Calculate the total spiciness of all slices.
    total_spiciness = sum(sorted_spiciness)
    
    # The minimum initial tolerance needed is the maximum spiciness of any slice.
    min_tolerance = max(sorted_spiciness[-1], total_spiciness - sorted_spiciness[-1])
    
    return min_tolerance

# Read input from stdin
n = int(input())
spiciness = list(map(int, input().split()))

# Output the result
print(min_initial_tolerance(n, spiciness))