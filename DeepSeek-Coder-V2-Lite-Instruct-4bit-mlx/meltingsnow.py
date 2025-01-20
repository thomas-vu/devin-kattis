def calculate_max_snow(S, P):
    if P == 100:
        return float(S)
    else:
        return S / (1 - P / 100.0)

# Read input
S, P = map(int, input().split())

# Calculate and output the result
print("{:.6f}".format(calculate_max_snow(S, P)))