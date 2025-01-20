def octal_to_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)[2:]  # Remove the '0x' prefix from the result
    return hexadecimal.upper()

# Read input
octal = input().strip()

# Convert and print the result
print(octal_to_hexadecimal(octal))