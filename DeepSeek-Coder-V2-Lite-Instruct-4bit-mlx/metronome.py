def calculate_revolutions(ticks):
    revolutions = ticks / 4.0
    return "{:.2f}".format(revolutions)

# Read the input
n = int(input())

# Calculate and output the result
print(calculate_revolutions(n))