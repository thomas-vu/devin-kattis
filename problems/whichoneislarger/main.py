def compare_decimals(a, b):
    # Split the decimals into integer and fractional parts
    a_int, a_frac = str(a).split('.')
    b_int, b_frac = str(b).split('.')
    
    # Convert fractional parts to integers for tuple comparison
    a_frac_int = int(a_frac) if a_frac != '0' else 0
    b_frac_int = int(b_frac) if b_frac != '0' else 0
    
    # Convert integer parts to integers for regular comparison
    a_int_val = int(a_int)
    b_int_val = int(b_int)
    
    # Compare the integer parts first
    if a_int_val > b_int_val:
        return float(a)
    elif a_int_val < b_int_val:
        return float(b)
    
    # If integer parts are equal, compare the fractional parts
    if a_frac_int > b_frac_int:
        return float(a)
    elif a_frac_int < b_frac_int:
        return float(b)
    
    # If both integer and fractional parts are equal, it's a special case
    return -1

# Read inputs
a = float(input())
b = float(input())

# Compare and print the result
result = compare_decimals(a, b)
print("%.2f" % result if result != -1 else -1)