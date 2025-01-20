def find_empty_space(N, P):
    # The pattern must be centered and symmetrically placed around the circumference.
    # Calculate the number of positions where the pattern can be centered without asymmetry.
    half_pattern = P // 2
    
    # Calculate the number of empty spaces left on the back of the sweater.
    empty_spaces = N - 2 * half_pattern
    
    return empty_spaces

# Read input from stdin
N, P = map(int, input().split())

# Output the result
print(find_empty_space(N, P))