import re
import sys

def find_hex_numbers(text):
    hex_pattern = r'0x[0-9A-Fa-f]+'
    hex_numbers = re.findall(hex_pattern, text)
    return hex_numbers

for line in sys.stdin:
    hex_numbers = find_hex_numbers(line)
    for number in hex_numbers:
        decimal_number = int(number, 16)
        print(f"{number} {decimal_number}")