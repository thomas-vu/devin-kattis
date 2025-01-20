import math

def expected_flips(c):
    if c == 1:
        return 0.0
    
    log2c = math.ceil(math.log2(c))
    expected_rounds = 0
    
    for i in range(log2c):
        p_success = (1 / c) * ((c - 1) / c) ** i
        expected_rounds += (i + 1) * p_success
    
    return log2c + expected_rounds / (1 - (c - 1) / c)

# Read the input
c = int(input().strip())

# Calculate and output the expected number of coin flips
print("{:.10f}".format(expected_flips(c)))