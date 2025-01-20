def expected_contestants(n, m):
    if n == 0:
        return float(m)
    elif m == 1:
        return 0.5
    else:
        # The probability that the glass tile breaks is 1/2 for each row, so the expected number of survivors after one step is m * (1 - 0.5^n)
        return m * ((1 - 2**-n) / (1 - 0.5))

# Read input from stdin
import sys
input_line = sys.stdin.readline().strip()
n, m = map(int, input_line.split())

# Calculate and print the expected number of contestants
expected = expected_contestants(n, m)
print("{:.12f}".format(expected))