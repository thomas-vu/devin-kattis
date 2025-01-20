def convert_to_roman_paces(x):
    conversion_factor = 1000 * (5280 / 4854)
    roman_paces = int(round(x * conversion_factor))
    return roman_paces

# Read input from stdin
import sys
input = sys.stdin.read
x = float(input().strip())

# Convert and print the result
print(convert_to_roman_paces(x))