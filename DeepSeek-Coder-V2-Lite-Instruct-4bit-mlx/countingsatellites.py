def generate_string(k):
    if k == 1:
        return "SATELLITE"
    
    # Start with the smallest possible string that can contain 1 "SATELLITE" subsequence
    s = ""
    while k > 0:
        # Determine the next part of the string to append
        if k % 2 == 1:
            s = "S" + s
            k //= 2
        else:
            s = "A" + s
            k //= 2
    
    # Ensure the string contains exactly "k" instances of "SATELLITE"
    expected_count = k
    actual_count = s.count("SATELLITE")
    
    while actual_count < expected_count:
        s = s + "SATELLITE"
        actual_count += 1
    
    return s

# Example usage:
k = int(input().strip())
print(generate_string(k))