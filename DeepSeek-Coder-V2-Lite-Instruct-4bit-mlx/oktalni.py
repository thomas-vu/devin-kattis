def binary_to_octal(binary_str):
    # Pad the binary string with zeros on the left until its length is divisible by 3
    while len(binary_str) % 3 != 0:
        binary_str = '0' + binary_str
    
    # Group adjacent binary digits into groups of 3
    grouped = [binary_str[i:i+3] for i in range(0, len(binary_str), 3)]
    
    # Replace each group of binary digits with the corresponding octal digit
    octal_str = ''
    for group in grouped:
        decimal_value = int(group, 2)
        octal_str += str(decimal_value)
    
    return octal_str

# Read input from stdin
binary_input = input().strip()

# Convert and print the result
print(binary_to_octal(binary_input))