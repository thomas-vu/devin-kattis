import sys

# Read input from stdin
input_line = sys.stdin.readline().strip()
a, b, c = map(int, input_line.split())

# Calculate the exact value of a * b / c
exact_value = (a * b) / c

# Output the exact value to 10 decimal places
sys.stdout.write(f"{exact_value:.10f}\n")