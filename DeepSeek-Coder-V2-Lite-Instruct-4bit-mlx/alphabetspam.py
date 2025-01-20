import sys

# Read input from stdin
input_line = sys.stdin.readline().strip()

# Initialize counters for each category
whitespace_count = 0
lowercase_count = 0
uppercase_count = 0
symbol_count = 0
total_chars = len(input_line)

# Count characters in each category
for char in input_line:
    if char == '_':
        whitespace_count += 1
    elif 'a' <= char <= 'z':
        lowercase_count += 1
    elif 'A' <= char <= 'Z':
        uppercase_count += 1
    else:
        symbol_count += 1

# Calculate ratios
whitespace_ratio = whitespace_count / total_chars
lowercase_ratio = lowercase_count / total_chars
uppercase_ratio = uppercase_count / total_chars
symbol_ratio = symbol_count / total_chars

# Output the results with the required precision
print("{:.16f}".format(whitespace_ratio))
print("{:.16f}".format(lowercase_ratio))
print("{:.16f}".format(uppercase_ratio))
print("{:.16f}".format(symbol_ratio))